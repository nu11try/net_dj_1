from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    template = 'catalog.html'

    if sort == "name":
        phones = Phone.objects.all().order_by('name')
    elif sort == "min_price":
        phones = Phone.objects.all().order_by('price')
    elif sort == "max_price":
        phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all()

    return render(request, template, {'phones': phones})


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
