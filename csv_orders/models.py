from django.db import models
from contractor_site_prices.models import ContractorSitePrice
from django.contrib.auth.models import User
from sor_entry.models import SOREntry

# Create your models here.

# CSV Download Order
class CSVOrder(models.Model):
    
    sor_entries = models.ManyToManyField(SOREntry)
    
    csp_entries = models.ManyToManyField(ContractorSitePrice)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    
    # Add entry 
    def add(self, item):
        
        # Determine type 
        if isinstance(item, SOREntry):
            self.sor_entries.add(item)
        else:
            self.csp_entries.add(item)
            
    # Remove entry 
    def remove(self, item):
        
        # Determine type 
        if isinstance(item, SOREntry):
            self.sor_entries.remove(item)
        else:
            self.csp_entries.remove(item)