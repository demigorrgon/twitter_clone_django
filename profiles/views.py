from django.shortcuts import render


def profile_view(request, *args, **kwargs):
    return render(request, "profiles/profile.html")
