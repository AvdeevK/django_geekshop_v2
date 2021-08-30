from django.shortcuts import render
from mainapp.models import Product

from basketapp.models import Basket


def index(request):
    title = 'Магазин'
    products = Product.objects.all()[:3]
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    context = {
        'title': title,
        'products': products,
    }
    return render(request, 'geekshop/index.html', context=context)


def contacts(request):
    title = 'Контакты'
    context = {
        'title': title
    }
    return render(request, 'geekshop/contact.html', context=context)