from django.views import generic



# Home page view 
class HomePage(generic.TemplateView):
    
    # Template 
    template_name = 'sor_pricing/home.html'