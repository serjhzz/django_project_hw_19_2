from django.shortcuts import render


def home_page(request):
    return render(request, 'catalog/home.html')


def contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{phone} - {name}: {message}')
    return render(request, 'catalog/contacts.html')


