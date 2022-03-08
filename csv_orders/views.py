from django.shortcuts import render
from .models import CSVOrder
from django.views import generic
from sor_entry.models import SOREntry
from contractor_site_prices.models import ContractorSitePrice
from django.http import HttpResponse, JsonResponse
import json
import csv

# Create your views here.

# Create an order list of SOR/CSP entries that need to be turned into a CSV
class UpdateCreateCSVOrder(generic.View):
    
    def post(self, *args, **kwargs):
        
        data = json.loads(self.request.body)
        
        # If the request is for a remove all operation
        if data['action'] == 'remove-all':
            return self.process_remove_all(data)
        else:
            return self.process_csp_sor(data)
        
    # Add or remove individual items
    def process_csp_sor(self, data):
        
        print(data)
        
        item_id = data['item_id']
        action = data['action']
        item_type = data['item_type']
        
        # Determine whether it is a csp or sor object 
        user = self.request.user
        if item_type == 'sor':
            item = SOREntry.objects.get(pk=item_id)
        else:
            item = ContractorSitePrice.objects.get(pk=item_id)
        
        # Get or create a download entry
        order, complete = CSVOrder.objects.get_or_create(user=user)
        
        # Add the object or delete based on action 
        if action == "add":
            order.add(item)
        else:
            order.remove(item)
        
        order.save()
        
        # Delete CSVOrder if there are no sor items in it 
        if (order.sor_entries.count() + order.csp_entries.count()) <= 0:
            order.delete()
            
        return JsonResponse({'DATA':data})
    
    # Remove an entire csp/sor list 
    def process_remove_all(self, data):
        
        action = data['action']
        item_type = data['item_type']
        
        # Determine which one to remove 
        order = CSVOrder.objects.get(user=self.request.user)
        if item_type == "sor":
            order.sor_entries.clear()
        else:
            order.csp_entries.clear()
            
        # Delete CSVOrder if there are no sor items in it 
        if (order.sor_entries.count() + order.csp_entries.count()) <= 0:
            order.delete()
            
        return JsonResponse({'DATA':data})
            
            
    

# "Cart" like page for viewing csv orders
class CSVOrderDetail(generic.DetailView):
    
    template_name = 'csv_orders/csv_orders.html'
    
    def get_object(self):
        
        # Get the users order
        try:
            query = CSVOrder.objects.get(user=self.request.user)
        except:
            query = None
            
        return query
    
    # Extra context data 
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        
        # CSV Order for this user 
        csv_order = self.get_object()
        
        # Add context
        context['title'] = "Order CSV"
        
        if csv_order:
            context['sor_orders'] = csv_order.sor_entries.all()
            context['csp_orders'] = csv_order.csp_entries.all()
            context['order_id'] = csv_order.pk
            
        return context
    
# Download SOR/CSP entries added to the "cart" as a csv/dat SEPARATELY
class DownloadOrder(generic.View):
    
    def get(self, *args, **kwargs):
        
        # Get the users Order
        obj = CSVOrder.objects.get(user=self.request.user)
        
        # Get item type 
        item_type = self.kwargs['item_type']
        query = obj.sor_entries.all() if item_type == "sor" else obj.csp_entries.all()
        
        # Create response 
        filename = "CON_SITE_PRICES" if item_type == "csp" else "SCHEDULE_OF_RATES"
        response = HttpResponse(
            content_type='text/csv',
            headers={
                'Content-Disposition': 'attachment; filename="{}.dat"'.format(filename)
            }
        )
        
        # Write the csv file 
        writer = csv.writer(response, quoting=csv.QUOTE_ALL)
        
        if item_type == 'sor':
            for entry in query:
                writer.writerow( entry.get_field_values_list() )
        
        else:
            for entry in query:
                for line in entry.get_csv_table_list():
                    line = [ '{}'.format(l) for l in line ]
                    writer.writerow( line )
        
        return response