from django.shortcuts import render
from django.http import HttpResponse


def cham(request):
    return HttpResponse('<h1><marquee> helllooo... chammm..</h1></marquee>')
