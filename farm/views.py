from django.shortcuts import render


def home(request):
    return render(request, 'farm/home.html', {'title': 'Home'})

def login(request):
    return render (request, 'users/login.html', {'title': 'Login'})

def farmer_detail(request):
    return render (request, 'farm/farmer_detail', {'title': 'Farmer_detail'})

def logout(request):
    return render (request, 'users/logout', {'title': 'Logout'})