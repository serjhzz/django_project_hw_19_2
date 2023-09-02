from django.contrib import admin

from catalog.models import Category, Product, Blog, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(Version)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product', 'number_version', 'is_activ',)
    list_filter = ('name',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'preview', 'created_at', 'is_published', 'view_count', 'slug',)
    list_filter = ('title',)
    search_fields = ('title', 'content')

