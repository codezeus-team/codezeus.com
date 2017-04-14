from django.shortcuts import render


def home(request):
    """Home Page"""
    context = {"title": "Development Studio"}
    return render(request, 'home.html', context)


def about(request):
    """About Page"""
    context = {"title": "About"}
    return render(request, 'about.html', context)


def contact(request):
    """Contact Page"""
    context = {"title": "Contact"}
    return render(request, 'contact.html', context)
