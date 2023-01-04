from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def products(request):
    template = loader.get_template('products.html')
    return HttpResponse(template.render())


def about_me(request):
    template = loader.get_template('aboutMe.html')
    return HttpResponse(template.render())
