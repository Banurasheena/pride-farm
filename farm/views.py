from django.shortcuts import render


def home(request):
    return render(request, 'users/login.html', {'title': 'Home'})

def login(request):
    return render (request, 'users/login.html', {'title': 'Login'})

def farmer_detail(request):
    return render (request, 'farm/farmer_detail.html', {'title': 'Farmer_detail'})

def logout(request):
    return render (request, 'users/logout.html', {'title': 'Logout'})

def officers(request):
    return render (request, 'farm/officers.html', {'title':'Officers'})