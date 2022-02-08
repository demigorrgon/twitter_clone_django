from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.


def login_view(request, *args, **kwargs):
    form = AuthenticationForm(request, data=request.POST)
    print(request.user.username)
    if form.is_valid():
        user_ = form.get_user()
        if user_:
            if user_.is_active:
                login(request, user_)
                messages.success(request, "Logged in")
                return redirect(reverse("frontpage"))

    context = {
        "form": form,
        "message": "Invalid username or password",
        "btn_text": "Login",
    }
    return render(request, "accounts/login.html", context)


def logout_view(request, *args, **kwargs):
    if request.method == "POST":
        logout(request)
        return redirect("login")

    context = {
        "description": "Are you sure you want to log out?",
        "btn_text": "Click to confirm",
    }
    return render(request, "accounts/logout.html", context)


def registration_view(request, *args, **kwargs):
    form = UserCreationForm(request.POST)
    print(request.user.username)
    if form.is_valid():
        user = form.save(commit=True)
        user.set_password(form.cleaned_data["password1"])
        login(request, user)
        messages.success(request, "Registered Successfully")
        return redirect(reverse("frontpage"))

    context = {"form": form, "btn_text": "Register"}
    return render(request, "accounts/register.html", context)
