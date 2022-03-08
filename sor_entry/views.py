from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse, JsonResponse
from django.utils import timezone 

from .filters import SORCodeFilter
from .models import *
from .forms import *

import csv
import json

# Create your views here.

###################################################
# SOR Entry
###################################################

# SOR create view 
class CreateSOR(generic.CreateView):
    
    # Model 
    model = SOREntry
    
    # Template 
    template_name = 'sor_entry/create_update_form.html'
    
    # Form
    form_class = SORForm 
    
    # Extra context data 
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        
        # Add context
        context['title'] = "New SOR"
        context['cancel_redirect'] = SOREntry.get_absolute_url(SOREntry)
        return context

# SOR detail view 
class SORDetail(generic.DetailView):
    
    model = SOREntry
    
    template_name = 'sor_entry/sor_detail.html'

# SOR list view 
class SORList(generic.ListView):
    
    model = SOREntry
    
    template_name = 'sor_entry/sor_list.html'
    
    # Filtered context data 
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        
        # Filter set 
        sor_filter = SORCodeFilter(self.request.GET, queryset=SOREntry.objects.all())
        
        if self.request.GET.get('date_created'):
            sorentry_list = sor_filter.qs
        else:
            sorentry_list = SOREntry.objects.all()
            
        # Query date 
        query_date = self.request.GET.get('date_created') if self.request.GET.get('date_created') else '-1'
        
        # Add context
        context['query_date'] = query_date
        context['sorentry_list'] = sorentry_list 
        context['sor_filter'] = sor_filter
        
        return context
    


###################################################
# LSOR_HRV_UOM_CODE
###################################################

# UOM create view
class CreateUOM(generic.CreateView):
    
    model = UOMCode
    
    template_name = 'sor_entry/create_update_form.html'
    
    form_class = UOMForm
    
    # Extra context data 
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        
        # Add context
        context['title'] = "New UOM Code"
        context['cancel_redirect'] = UOMCode.get_absolute_url(UOMCode)
        return context

# SOR list view 
class UOMList(generic.ListView):
    
    model = UOMCode
    
    template_name = 'sor_entry/uom_list.html'
    


###################################################
# LSOR_HRV_TRD_CODE
###################################################

# TRD create view
class CreateTRD(generic.CreateView):
    
    model = TRDCode
    
    template_name = 'sor_entry/create_update_form.html'
    
    form_class = TRDForm
    
    # Extra context data 
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        
        # Add context
        context['title'] = "New TRD Code"
        context['cancel_redirect'] = TRDCode.get_absolute_url(TRDCode)
        return context

# TRD list view 
class TRDList(generic.ListView):
    
    model = TRDCode
    
    template_name = 'sor_entry/trd_list.html'



###################################################
# LSOR_HRV_LOC_CODE
###################################################

# LOC create view
class CreateLOC(generic.CreateView):
    
    model = LOCCode
    
    template_name = 'sor_entry/create_update_form.html'
    
    form_class = LOCForm
    
    # Extra context data 
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        
        # Add context
        context['title'] = "New LOC Code"
        context['cancel_redirect'] = LOCCode.get_absolute_url(LOCCode)
        return context

# LOC list view 
class LOCList(generic.ListView):
    
    model = LOCCode
    
    template_name = 'sor_entry/loc_list.html'
    


###################################################
# LSOR_PRI_CODE
###################################################

# PRI create view
class CreatePRI(generic.CreateView):
    
    model = LOCCode
    
    template_name = 'sor_entry/create_update_form.html'
    
    form_class = PRIForm
    
    # Extra context data 
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        
        # Add context
        context['title'] = "New PRI Code"
        context['cancel_redirect'] = PRICode.get_absolute_url(PRICode)
        return context

# LOC list view 
class PRIList(generic.ListView):
    
    model = PRICode
    
    template_name = 'sor_entry/pri_list.html'



###################################################
# CSV Download
###################################################

# Download a CSV file from a single model
class DownloadCSVSingle(generic.View):
    
    def get(self, *args, **kwargs):
        
        # Get the queried object
        obj = SOREntry.objects.get(pk=self.kwargs['pk'])
        
        # Create response 
        response = HttpResponse(
            content_type='text/csv',
            headers={
                'Content-Disposition': 'attachment; filename="{}.DAT"'.format(obj.lsor_code)
            }
        )
        
        # Write the CSV file
        writer = csv.writer(response, quoting=csv.QUOTE_ALL)
        writer.writerow(obj.get_field_values_list())
        
        return response

# Download SOR entries with a specific date as a csv
class DownloadCSVDate(generic.View):
    
    def get(self, *args, **kwargs):
        
        # Query for SOR entries with date_created as a filter
        date_created = self.kwargs['date_created']
        
        if date_created != '-1':
            sor_entries = SOREntry.objects.filter(date_created__date=date_created)
        else:
            sor_entries = SOREntry.objects.all()
        
        # Create response 
        response = HttpResponse(
            content_type='text/csv',
            headers={
                'Content-Disposition': 'attachment; filename="SOR_LIST.DAT"'
            }
        )
        
        # Write the CSV file
        writer = csv.writer(response, quoting=csv.QUOTE_ALL)
        for sor in sor_entries.all():
            writer.writerow(sor.get_field_values_list())
            
        return response