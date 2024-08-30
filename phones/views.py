from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    phone = Phone.objects.all()
    if sort == 'name':
        phone = phone.order_by('name')
    elif sort == 'min_price':
        phone = phone.order_by('price')
    elif sort == 'max_price':
        phone = phone.order_by('-price')
    else:
        phone = phone.order_by('id')
    context = {
        'phones': phone
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    slug = Phone.objects.get(slug=slug)
    context = {
        'phone': slug
    }
    return render(request, template, context)
