from django.shortcuts import render, HttpResponse


def login(request):
    if request.method == 'POST':
        return HttpResponse('Hello Login')

    return HttpResponse('Invalid Access')


def register(request):
    if request.method == 'POST':
        return HttpResponse('Hello Register')

    return HttpResponse('Invalid Access')
