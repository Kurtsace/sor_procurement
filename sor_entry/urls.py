from django.urls import path, include
from .views import *

app_name = 'sor_entry'

urlpatterns = [
    path('new_sor/', CreateSOR.as_view(), name='create_sor'),
    path('sor_list/', SORList.as_view(), name='sor_list'),
    path('sor_detail/<int:pk>/', SORDetail.as_view(), name='sor_detail'),
    
    path('new_uom/', CreateUOM.as_view(), name='create_uom'),
    path('uom_list/', UOMList.as_view(), name='uom_list'),
    
    path('new_trd/', CreateTRD.as_view(), name='create_trd'),
    path('trd_list/', TRDList.as_view(), name='trd_list'),
    
    path('new_loc/', CreateLOC.as_view(), name='create_loc'),
    path('loc_list/', LOCList.as_view(), name='loc_list'),
    
    path('new_pri/', CreatePRI.as_view(), name='create_pri'),
    path('pri_list/', PRIList.as_view(), name='pri_list'),
    
    path('get_single_csv/<int:pk>/', DownloadCSVSingle.as_view(), name="download_single_csv"),
]
