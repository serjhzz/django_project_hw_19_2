from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from catalog.models import Product, Blog


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'object_list'
    paginate_by = 10


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'
    context_object_name = 'object'
    pk_url_kwarg = 'pk'


class ContactsView(View):
    def get(self, request):
        return render(request, 'catalog/contacts.html')


class BlogListView(ListView):
    model = Blog
    extra_context = {'title': 'Blogs'}
    template_name = 'blog/blog_list.html'


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title','slug', 'content', 'preview')
    extra_context = {'title': 'Create blog'}
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:blog_list')


class BlogDetailView(DetailView):
    model = Blog
    extra_context = {'title': 'Blog'}
    template_name = 'blog/blog_detail.html'


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content',)
    template_name = 'blog/blog_form.html'
    extra_context = {'title': 'Update blog'}
    success_url = reverse_lazy('blogs:blog_list')


class BlogDeleteView(DeleteView):
    model = Blog
    extra_context = {'title': 'Delete blog'}
    success_url = reverse_lazy('blogs:blog_list')
    template_name = 'blog/blog_confirm_delete.html'






