from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect


def rawText(request):
    return HttpResponse("this is the rawText")


def rawHtml(req):
    # 这里render的可以是任意一个app下的templates
    return render(req, "rawHtml.html")


def useTemplate(req):
    return render(req, 'include/base.html')


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        print("User.getName")
        return self.name


def passParam(req):
    return render(req, "passParam.html", {
        'string': 'weidiao is great',
        'list': ['one', 'two', 'three'],
        'dic': {'one': 1, 'two': 2, 'three': 3},
        'numbers': [[i for i in range(1, 2, 10)], [i for i in range(1, 3, 10)], [i for i in range(1, 4, 10)]],
        'user': User('weidiao', 24)
    })


def redirect(req):
    return HttpResponseRedirect("/")


def extends(req):
    return render(req, "include/extends.html")


def includeExtends(req):
    return render(req, "include/includeExtends.html")
