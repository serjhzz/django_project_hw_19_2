from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Blog, Version


class ProductListView(ListView):
    model = Product
    extra_context = {'title': 'Product'}
    template_name = 'catalog/catalog_list.html'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        active_versions = Version.objects.filter(is_activ=True)
        context['active_versions'] = active_versions
        return context


class ProductDetailView(DetailView):
    model = Product
    extra_context = {'title': 'Detail'}
    template_name = 'catalog/catalog_detail.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    extra_context = {'title': 'Create product'}
    template_name = 'catalog/catalog_form.html'
    success_url = reverse_lazy('catalog:catalog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.save()

        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/catalog_form.html'
    extra_context = {'title': 'Update product'}
    success_url = reverse_lazy('catalog:catalog_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    extra_context = {'title': 'Delete product'}
    success_url = reverse_lazy('catalog:catalog_list')
    template_name = 'catalog/catalog_confirm_delete.html'


class ContactsView(View):
    def get(self, request):
        return render(request, 'catalog/contacts.html')


class BlogListView(ListView):
    model = Blog
    extra_context = {'title': 'Blogs'}
    template_name = 'blog/blog_list.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'is_published')
    extra_context = {'title': 'Create blog'}
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = Blog
    extra_context = {'title': 'Blog'}
    template_name = 'blog/blog_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content',)
    template_name = 'blog/blog_form.html'
    extra_context = {'title': 'Update blog'}
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogDeleteView(DeleteView):
    model = Blog
    extra_context = {'title': 'Delete blog'}
    success_url = reverse_lazy('blog:blog_list')
    template_name = 'blog/blog_confirm_delete.html'






