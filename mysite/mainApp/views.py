from django.shortcuts import render
from .forms import SubscribersForm
from products.models import *


def index(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    form = SubscribersForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        print(data["name"])
        new_form = form.save()

    return render(request, 'mainApp/all.html', locals())


def id1(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_100 = products_images.filter(product__category__id=1)
    return render(request, 'mainApp/100.html', locals())


def id2(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_100_150 = products_images.filter(product__category__id=2)
    return render(request, 'mainApp/100_150.html', locals())

def id3(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_150 = products_images.filter(product__category__id=3)
    return render(request, 'mainApp/150.html', locals())
