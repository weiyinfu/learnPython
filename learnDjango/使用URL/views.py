from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def add(req):
    a = req.GET['a']
    b = req.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(req, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def useName(req):
    return render(req, "useName.html")
