from django.shortcuts import render


# Create your views here.
def test_view(request, *args, **kwargs):
    return render(request, "pages/index.html")
