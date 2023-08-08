from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home_page, contact_page, product_page

app_name = CatalogConfig.name

urlpatterns = [
    path('', home_page, name='home_page'),
    path('contacts/', contact_page, name='contact_page'),
    path('product/<int:pk>/', product_page, name='product_page')
]
