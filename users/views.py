from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.contrib.auth import authenticate, login, logout

# Create your views here.

class NewLoginForm(forms.Form):
    username = forms.CharField()

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "users/index.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        return render(request, "users/login.html", {
            "message": "Invalid credentials"
        })

    return render(request, "users/login.html")

def user_logout(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged out successfully",
    })