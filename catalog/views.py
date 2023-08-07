from django.shortcuts import render

from catalog.models import Product


def home_page(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Главная'
    }
    return render(request, 'catalog/home.html', context)


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


