from django.shortcuts import render
from django.contrib.auth import logout as django_logout


def home(request):
    return render(request, "users/register.html", {})


def logout(request):
    django_logout(request)
    return render(request, "main/logout.html")

# def login_view(request):
#     return render(request, 'users/login.html')
