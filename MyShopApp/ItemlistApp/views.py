from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from .models import ClothItem, User


# Create your views here.


def index(request, id):
    item = ClothItem.objects.get(id=id)
    return HttpResponse('<h1>%s</h1>' % item.name)
