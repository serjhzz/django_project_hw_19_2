from django.shortcuts import render

from catalog.models import Product


def home_page(request):
    product_list = Product.objects.all()[:3]
    context = {
        'object_list': product_list,
        'title': 'Главная'
    }
    return render(request, 'catalog/home.html', context)


def product_page(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(id=pk),
        'title': 'Товары'
    }
    return render(request, 'catalog/product.html', context)


def contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{phone} - {name}: {message}')
    context = {
        'title': 'Контакты',
    }
    return render(request, 'catalog/contacts.html', context)


