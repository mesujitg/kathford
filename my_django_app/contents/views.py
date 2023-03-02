from django.shortcuts import render, HttpResponse


def show_home(request):
    return render(request, 'index.html')


def show_about(request):
    return HttpResponse('About Us')


def show_contacts(request):
    return HttpResponse('Contact Us')


def show_policies(request):
    return HttpResponse('Policies')