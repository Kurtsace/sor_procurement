from django import forms 

from .models import *


# CSP Create/Update Form 
class CSPForm(forms.ModelForm):
    
    class Meta: 
        
        model = ContractorSitePrice
        
        exclude = ['lcspg_ppc_ppp_start_date', 'cspg_end_date', 'lcsp_preferred_ind', 'user']
        
        widgets = {
            'cspg_start_date': forms.DateInput({'type':'date'}),
            'lcspg_ppp_ppg_code': forms.CheckboxSelectMultiple(),
            'lcspg_ppp_wpr_code':forms.CheckboxSelectMultiple(),
        }