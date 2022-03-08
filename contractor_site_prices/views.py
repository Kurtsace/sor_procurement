from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .forms import *
from .models import *
import csv

# Create your views here.

###################################################
# Contractor Site Prices 
###################################################

# CSP create view 
class CreateCSP(generic.CreateView):
    
    # Model 
    model = ContractorSitePrice
    
    # Template 
    template_name = 'contractor_site_prices/create_update_form.html'
    
    # Form
    form_class = CSPForm 
    
    # Extra context data 
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        
        # Add context
        context['title'] = "New CSP"
        context['cancel_redirect'] = ContractorSitePrice.get_absolute_url(ContractorSitePrice)
        return context
    
# CSP List 
class CSPList(generic.ListView):
    
     # Model 
    model = ContractorSitePrice
    
    # Template 
    template_name = 'contractor_site_prices/csp_list.html'
    
# CSP Detail
class CSPDetail(generic.DetailView):
    
    model = ContractorSitePrice
    
    template_name = 'contractor_site_prices/csp_detail.html'
    
    
    
###################################################
# Contractor Site Prices CSV Download 
###################################################

# Get single CSP as a csv 
class CSPDownloadSingle(generic.View):
    
    def get(self, *args, **kwargs):
        
        # Get the object 
        csp = ContractorSitePrice.objects.get(pk=self.kwargs['pk'])
        
        # Create a response 
        response = HttpResponse(
            content_type='text/csv',
            headers={
                'Content-Disposition': 'attachment; filename="CON_SITE_PRICES_{}_1.dat'
            }
        )
        
        # Write the csv file 
        writer = csv.writer(response, quoting=csv.QUOTE_ALL)
        for line in csp.get_csv_table_list():
            line = [ '{}'.format(l) for l in line ]
            row = ",".join(line)
            writer.writerow( line )
            
        return response
    
