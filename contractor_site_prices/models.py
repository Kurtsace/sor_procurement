from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from sor_entry.models import SOREntry

# Create your models here.

# Policy code
# LPPC_PPP_PPG_CODE
class PolicyCode(models.Model):
    
    lppc_ppp_ppg_code = models.CharField(max_length=10, unique=True, blank=False, null=False, verbose_name="Pricing Policy Group Code")
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.lppc_ppp_ppg_code

# Work programme
# LPPC_PPP_WPR_CODE
class WorkProgramme(models.Model):
    
    lppc_ppp_wpr_code = models.CharField(max_length=10, unique=True, blank=False, null=False, verbose_name="Work Programme")
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.lppc_ppp_wpr_code
    
# Contractor Site Prices 
class ContractorSitePrice(models.Model):
    
    lcspg_ppp_ppg_code = models.ManyToManyField(PolicyCode, blank=False, verbose_name="Policy Code")
    
    lcspg_ppp_wpr_code = models.ManyToManyField(WorkProgramme, blank=False, verbose_name="Work Programme")
    
    lcspg_ppc_ppp_start_date = models.DateField(default="2016-05-12", verbose_name="Policy Start Date")
    
    lcspg_ppc_cos_code = models.CharField(max_length=15, blank=False, null=False, verbose_name="Contractor Site Code")
    
    cspg_start_date = models.DateField(default="2016-05-12", verbose_name="Contract Start Date")
    
    cspg_end_date = models.DateField(blank=True, null=True, verbose_name="Contract End Date")
    
    lcsp_sor_code = models.ForeignKey(SOREntry, on_delete=models.CASCADE, verbose_name="SOR Code")
    
    lcsp_price = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False, verbose_name="Price")
    
    lcsp_preferred_ind = models.CharField(max_length=1, blank=False, null=False, default="N", verbose_name="Preferred Ind")
    
    ##########################
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    
    date_created = models.DateTimeField(auto_now_add=True)
    
    def get_value_list_slice(self, start, stop):
        
        # Generate values 
        values = []
        
        # Get field values in proper formats 
        for field in self._meta.get_fields()[start:stop]:
            
            value = getattr(self, field.name)
            
            if value == None:
                values.append("")
            
            # Reformat datefield
            elif isinstance(field, models.DateField):
                values.append( value.strftime("%d-%b-%Y") )
                
            else:
                values.append(value)
        
        return values
    
    # Return a CSV ready table in array form 
    def get_csv_table_list(self):
        
        # Get base template 
        template = self.get_value_list_slice(2, -4)
        
        # Generate each row
        csv_table = []
        for policy in self.lcspg_ppp_ppg_code.all():
            
            for work_programme in self.lcspg_ppp_wpr_code.all():
                
                # Generate the row 
                csv_table.append( [policy.lppc_ppp_ppg_code, work_programme.lppc_ppp_wpr_code] + template )

        return csv_table
    
    # Redirect 
    def get_absolute_url(self):
        return reverse('contractor_site_prices:csp_list')
    
    def __str__(self):
        return "CSP_{}".format(self.id)