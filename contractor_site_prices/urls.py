from django.urls import path, include
from .views import *

app_name = 'contractor_site_prices'

urlpatterns = [
    
    path('new_csp/', CreateCSP.as_view(), name='create_csp'),
    path('csp_list/', CSPList.as_view(), name='csp_list'),
    path('csp_detail/<int:pk>/', CSPDetail.as_view(), name='csp_detail'),
    
    path('download_single_csv/<int:pk>/', CSPDownloadSingle.as_view(), name='get_single_csv'),
]