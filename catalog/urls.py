from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home_page, contact_page, product_page, BlogListView, BlogCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', home_page, name='home_page'),
    path('contacts/', contact_page, name='contact_page'),
    path('product/<int:pk>/', product_page, name='product_page'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_form'),
    # path('blog/<slug:slug>/', ..., name='entry_detail'),
    # path('blog/<slug:slug>/update/', ..., name='entry_update'),
    # path('blog/<slug:slug>/delete/', ..., name='entry_delete'),
]
