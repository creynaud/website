from django.shortcuts import render


def home(request):
    response = render(request, "home.html")
    return response


def resume(request):
    response = render(request, "resume.html")
    return response


def sitemap(request):
    response = render(request, "sitemap.xml")
    return response
