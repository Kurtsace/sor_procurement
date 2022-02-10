from django import forms 
from .models import *

# SOR Create/Update form 
class SORForm(forms.ModelForm):
    
    class Meta: 
        
        model = SOREntry
        
        fields = ['lsor_code', 'lsor_description', 'lsor_reorder_period_no', 'lsor_price', 'lsor_pri_code', 'lsor_hrv_trd_code', 'lsor_hrv_uom_code', 'lsor_hrv_loc_code',]
        
# UOM Create/Update form 
class UOMForm(forms.ModelForm):
    
    class Meta: 
        
        model = UOMCode
        
        fields = ['lsor_hrv_uom_code']
        

# TRD Create/Update form 
class TRDForm(forms.ModelForm):
    
    class Meta: 
        
        model = TRDCode
        
        fields = ['lsor_hrv_trd_code']
        
# LOC Create/Update form 
class LOCForm(forms.ModelForm):
    
    class Meta: 
        
        model = LOCCode 
        
        fields = ['lsor_hrv_loc_code']
        
# LOC Create/Update form 
class PRIForm(forms.ModelForm):
    
    class Meta: 
        
        model = PRICode 
        
        fields = ['lsor_pri_code']
        
        

