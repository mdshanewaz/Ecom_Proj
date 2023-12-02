from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse

# Authentications
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# Messagaes 
from django.contrib import messages

# Forms and Models
from Login_App.models import ProfileModel, User
from Login_App.forms import ProfileForm, SignupForm


# Create your views here.
def signupView(request):
    title = 'SIGNUP'
    form = SignupForm
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully!")
            return HttpResponseRedirect(reverse('Login_App:login'))
    return render(request, 'Login_App/signup.html', context={'title':title, 'form':form})

def loginView(request):
    title = 'LOGIN'
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('Shop_App:home'))
    return render(request, 'Login_App/login.html', context={'title': title, 'form':form})

@login_required
def logoutView(request):
    logout(request)
    messages.warning(request, "You are logged out!")
    return HttpResponseRedirect(reverse('Shop_App:home'))

@login_required
def user_profileView(request):
    title = 'Profile'
    profile = ProfileModel.objects.get(user=request.user)
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Changes are saved to Profile!")
            form = ProfileForm(instance=profile)
    return render(request, 'Login_App/change_profile.html', context={'title':title, 'form':form})