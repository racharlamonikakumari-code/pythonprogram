from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('welcome')
    else:
        form = UserCreationForm()
    return render(request, 'studentapp/register.html', {'form': form})

@login_required
def welcome(request):
    return render(request, 'studentapp/welcome.html')

def logout_view(request):
    logout(request)
    return redirect('login')
