from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import LoginForm

# Create your views here.


def login_view(request, *args, **kwargs):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect("/")
        context = {"form": form, "message": "Invalid username or password"}
        return render(request, "pages/login.html", context)


def logout_view(request, *args, **kwargs):
    if request.method == "POST":
        logout(request)
        return redirect("/login")

    context = {
        "description": "Are you sure you want to log out?",
        "btn_text": "Click to confirm",
    }
    return render(request, "pages/logout.html", context)


def registration_view(request, *args, **kwargs):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save(commit=True)
        user.set_password(form.cleaned_data["password1"])
        login(request, user)
        return redirect("/")

    context = {"form": form, "btn_text": "Register"}
    return render(request, "pages/registration.html", context)
