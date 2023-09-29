from django.shortcuts import HttpResponse


def login(request):
    if request.method is "POST":
        ret = HttpResponse()
        return ret
