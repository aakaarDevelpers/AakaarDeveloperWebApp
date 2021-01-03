from django.shortcuts import render, redirect

# Credentials Forms
from .forms import CustomUserRegisterForm, CustomUserloginForm

# Authentication Functions
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Message Framework
from django.contrib import messages

def user_auth(request):

    register_form = CustomUserRegisterForm()
    login_form = CustomUserloginForm()

    if request.method == 'POST':
        register_form = CustomUserRegisterForm( request.POST or None )

        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')

            register_form.save()
            messages.success(request, f'{username}, Your Account is Created!!!')
            return redirect('authentication_page')

    context = {}
    context['register_form'] = register_form
    context['login_form'] = login_form

    return render(request, 'users/auth.html', context)

def login_user(request):

    if request.method == 'POST':
        form = CustomUserloginForm( request.POST or None )

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                messages.success(request, f'{username}, You Have Successfully Logged in')
                return redirect('homepage')

            else:
                messages.success(request, f'{username}, Try With Correct Credentials')
                return redirect('authentication_page')

def user_logout(request):
    logout(request)
    return redirect('homepage')