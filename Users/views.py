from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        context = {
            'first_name' : request.POST['first_name'],
            'last_name' : request.POST['last_name'],
            'email' : request.POST['email'],
            'username' : request.POST['username'],
            'password' : request.POST['password'],
            'password2' : request.POST['password2'],
        }
        user_exists = User.objects.filter(username=context['username']).exists()

        if context['password'] == context['password2'] and not user_exists:
            new_user = User.objects.create_user(
                first_name = context['first_name'],
                last_name = context['last_name'],
                email = context['email'],
                username = context['username'],
                password = context['password']
            )
            new_user.save()
        
            return redirect('login')
        else:
            return render(request, 'accounts/register.html', context)
    else: 
        return render(request, 'accounts/register.html')
    
def user_login(request):
    if request.method == 'POST':
        user = authenticate(
            username = request.POST['username'], 
            password = request.POST['password'] 
            )

        if user is not None: 
            login(request, user)
        print('login user here')

        return render(request, 'accounts/dashboard.html')
    else:
        return render(request, 'accounts/login.html')


def user_logout(request):
    logout(request)
    return redirect('index')

@login_required
def dashboard(request):
    pass
