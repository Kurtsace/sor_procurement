from django.urls import path, include
from .views import *

app_name = 'csv_orders'

urlpatterns = [
    
    path('update_item/', UpdateCreateCSVOrder.as_view(), name='update_item'),
    path('csv_orders/', CSVOrderDetail.as_view(), name='orders'),
    path('download_order/<str:item_type>', DownloadOrder.as_view(), name='download_order')
]