"""sor_pricing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import HomePage

app_name = 'sor_pricing'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name='home'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('sor_entry/', include('sor_entry.urls', namespace='sor_entry')),
    path('pricing_policy/', include('pricing_policy_entry.urls', namespace='pricing_policy_entry')),
    path('contractor_site_prices/', include('contractor_site_prices.urls', namespace='contractor_site_prices')),
    path('csv_orders/', include('csv_orders.urls', namespace='csv_orders'))
]
