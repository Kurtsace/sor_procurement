from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from csv import reader 
from datetime import datetime

# Create your models here.

# Units of measure code 
# LSOR_HRV_UOM_CODE 
class UOMCode(models.Model):
    
    # Fields 
    lsor_hrv_uom_code = models.CharField(max_length=10, blank=False, null=False, unique=True, verbose_name="LSOR_HRV_UOM_CODE")
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True) 
    
    date_created = models.DateTimeField(auto_now_add=True)
    
    # Redirect
    def get_absolute_url(self):
        return reverse('sor_entry:uom_list')
    
    # STR representation
    def __str__(self):
        return self.lsor_hrv_uom_code
    


# Trade code 
# LSOR_HRV_TRD_CODE
class TRDCode(models.Model):
    
    # Fields 
    lsor_hrv_trd_code = models.CharField(max_length=10, blank=False, null=False, unique=True, verbose_name="LSOR_HRV_TRD_CODE")

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True) 
    
    date_created = models.DateTimeField(auto_now_add=True)
    
    # Redirect
    def get_absolute_url(self):
        return reverse('sor_entry:trd_list')
    
    # STR representation
    def __str__(self):
        return self.lsor_hrv_trd_code
    
    
# Location code 
# LSOR_HRV_LOC_CODE
class LOCCode(models.Model):
    
    # Fields 
    lsor_hrv_loc_code = models.CharField(max_length=10, blank=False, null=False, unique=True, verbose_name="LSOR_HRV_LOC_CODE")
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True) 
    
    date_created = models.DateTimeField(auto_now_add=True)
    
    # Redirect
    def get_absolute_url(self):
        return reverse('sor_entry:loc_list')
    
    # STR representation
    def __str__(self):
        return self.lsor_hrv_loc_code
    


# Priority code 
# LSOR_PRI_CODE
class PRICode(models.Model):
    
    # Fields 
    lsor_pri_code = models.CharField(max_length=3, blank=False, null=False, unique=True, verbose_name="LSOR_PRI_CODE")
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True) 
    
    date_created = models.DateTimeField(auto_now_add=True)
    
    # Redirect
    def get_absolute_url(self):
        return reverse('sor_entry:pri_list')
    
    # STR representation
    def __str__(self):
        return self.lsor_pri_code



# Sor entry models
class SOREntry(models.Model):
    
    # Fields 
    lsor_code = models.CharField(max_length=10, blank=False, null=False, unique=True, verbose_name="LSOR_CODE")
    
    lsor_type = models.CharField(max_length=1, blank=False, null=False, default="S", verbose_name="LSOR_TYPE")
    
    lsor_description = models.TextField(max_length=4000, blank=False, null=False, verbose_name="LSOR_DESCRIPTION")
    
    lsor_start_date = models.DateField(default="2016-05-16", verbose_name="LSOR_START_DATE")
    
    lsor_current_ind = models.CharField(max_length=1, default="Y", verbose_name="LSOR_CURRENT_IND")
    
    lsor_pre_inspect_ind = models.CharField(max_length=1, blank=False, null=False, default="N", verbose_name="LSOR_PRE_INSPECT_IND")
    
    lsor_post_inspect_ind = models.CharField(max_length=1, blank=False, null=False, default="N", verbose_name="LSOR_POST_INSPECT_IND")
    
    lsor_hrv_itt_code = models.CharField(max_length=10, blank=False, null=False, default="SOR", verbose_name="LSOR_HRV_ITT_CODE")
    
    lsor_end_date =  models.DateField(blank=True, null=True)
    
    lsor_reorder_period_no = models.IntegerField(null=False, blank=False, default=12, verbose_name="LSOR_REORDER_PERIOD_NO")
    
    lsor_reorder_period_unit = models.CharField(max_length=1, null=False, blank=False, default="M", verbose_name="LSOR_REORDER_PERIOD_UNIT")
    
    lsor_warranty_period_no = models.IntegerField(null=True, blank=True, verbose_name="LSOR_WARRANTY_PERIOD_NO")
    
    lsor_warranty_period_unit = models.CharField(max_length=1, null=False, blank=False, default="M", verbose_name="LSOR_WARRANTY_PERIOD_UNIT")
    
    lsor_keywords = models.CharField(max_length=240, null=False, blank=True, default="", verbose_name="LSOR_KEYWORDS")
    
    lsor_pri_code = models.ForeignKey(PRICode, on_delete=models.CASCADE, blank=False, null=True, verbose_name="LSOR_PRI_CODE")
    
    lsor_hrv_vca_code = models.CharField(max_length=10, null=False, blank=True, default="", verbose_name="LSOR_HRV_VCA_CODE")
    
    lsor_hrv_trd_code = models.ForeignKey(TRDCode, on_delete=models.CASCADE, blank=False, null=True, verbose_name="LSOR_HRV_TRD_CODE")
    
    lsor_hrv_lia_code = models.CharField(max_length=10, null=False, blank=False, default="AUT", verbose_name="LSOR_HRV_LIA_CODE")
    
    lsor_arc_sys_code = models.CharField(max_length=3, null=False, blank=False, default="AUT", verbose_name="LSOR_ARC_SYS_CODE")
    
    lsor_hrv_uom_code = models.ForeignKey(UOMCode, on_delete=models.CASCADE, blank=False, null=True, verbose_name="LSOR_HRV_UOM_CODE")
    
    lsor_wdc_code = models.CharField(max_length=10, null=False, blank=True, default="", verbose_name="LSOR_WDC_CODE")
    
    lsor_liability_type_ind = models.CharField(max_length=1, null=False, blank=False, default="O", verbose_name="LSOR_LIABILITY_TYPE_IND")
    
    lsor_price = models.DecimalField(max_digits=11, decimal_places=2, null=False, blank=False, verbose_name="LSOR_PRICE")
    
    lsor_price_start_date = models.DateField(default="2016-05-16", verbose_name="LSOR_PRICE_START_DATE")
    
    lsor_price_end_date = models.DateField(blank=True, null=True, verbose_name="LSOR_PRICE_END_DATE")
    
    lsor_coverage_amount = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name="LSOR_COVERAGE_AMOUNT")
    
    lsor_hrv_jcl_code = models.CharField(max_length=10, null=False, blank=True, default="", verbose_name="LSOR_HRV_JCL_CODE")
    
    lsor_quantity = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, default=1, verbose_name="LSOR_QUANTITY")
    
    lsor_hrv_loc_code = models.ForeignKey(LOCCode, on_delete=models.CASCADE, blank=False, null=True, verbose_name="LSOR_HRV_LOC_CODE")
    
    lsor_arc_code = models.CharField(max_length=3, unique=False, null=False, blank=False, default="HRM", verbose_name="LSOR_ARC_CODE")
    
    lsor_repeat_unit = models.IntegerField(null=True, blank=True, verbose_name="LSOR_REPEAT_UNIT")
    
    lsor_repeat_period_ind = models.CharField(max_length=1, null=False, blank=True, default="", verbose_name="LSOR_REPEAT_PERIOD_IND")
    
    lsor_hrm_element_update = models.CharField(max_length=1, null=False, blank=False, default="Y", verbose_name="LSOR_HRM_ELEMENT_UPDATE")
    
    lsor_hpm_element_update = models.CharField(max_length=1, null=False, blank=False, default="Y", verbose_name="LSOR_HPM_ELEMENT_UPDATE")
    
    lsor_allow_break_ind = models.CharField(max_length=1, null=False, blank=False, default="Y", verbose_name="LSOR_ALLOW_BREAK_IND")
    
    lsor_code_mlang = models.CharField(max_length=10, null=False, blank=True, default="", verbose_name="LSOR_CODE_MLANG")
    
    lsor_description_mlang = models.TextField(max_length=4000, null=False, blank=True, default="", verbose_name="LSOR_DESCRIPTION_MLANG")
    
    lsor_keywords_mlang = models.CharField(max_length=240, null=False, blank=True, default="", verbose_name="LSOR_KEYWORDS_MLANG")
    
    
    ##########################
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    
    date_created = models.DateTimeField(auto_now_add=True)
    
    # Redirect
    def get_absolute_url(self):
        return reverse('sor_entry:sor_list')
    
    # Return field values list 
    # Remove the first and last two values in the list as they are not needed 
    def get_field_values_list(self):
        
        values = []
        
        # Build the list 
        for field in self._meta.get_fields()[2:-2]:
            
            value = getattr(self, field.name)
            
            if value == None:
                values.append("")
            
            # Reformat datefield
            elif isinstance(field, models.DateField):
                values.append( value.strftime("%d-%b-%Y") )
                
            else:
                values.append(value)
                
        return values
    
    # Get CSV rows 
    # Return get_field_values_list() as a CSV row 
    def get_csv_row(self):
        return ','.join([ '"{}"'.format(val) for val in self.get_field_values_list() ])
    
    # Return the field,value tuple 
    def get_key_val_tuple(self):
        
        fields = [ field.name for field in self._meta.get_fields() ][2:-2]
        values = self.get_field_values_list()
        
        return zip(fields, values)
    
    # STR representation
    def __str__(self):
        return self.lsor_code
    
    
# SOR CSV Download Order
class SORCSVOrder(models.Model):
    
    sor_entries = models.ManyToManyField(SOREntry)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)