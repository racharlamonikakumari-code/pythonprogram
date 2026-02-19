from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def checkout(request):
    return render(request, 'checkout.html')

def place_order(request):
    return render(request, 'checkout.html')  # or order_success.html later
