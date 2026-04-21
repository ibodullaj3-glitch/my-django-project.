from django.shortcuts import render

def home(request):
    user = {"username": "Joraboyev"}
    return render(request, 'home.html', {'user': user})


def about(request):
    user = {"username": "Admin"}
    return render(request, 'about.html', {'user': user})