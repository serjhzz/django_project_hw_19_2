from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactsView, ProductDetailView, BlogListView, BlogCreateView, \
    BlogDetailView, \
    BlogUpdateView, BlogDeleteView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='catalog_list'),
    path('product/create/', ProductCreateView.as_view(), name='catalog_form'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='catalog_detail'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='catalog_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='catalog_delete'),

    path('contacts/', ContactsView.as_view(), name='contact_page'),

    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_form'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
]
