from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(u"Hello World 学而时习之")
