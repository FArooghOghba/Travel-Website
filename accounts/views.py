from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'GET':
        return render(request, 'accounts/login.html')
    elif request.method == 'POST':
        authenticate_form = AuthenticationForm(request=request, data=request.POST)
        if authenticate_form.is_valid():
            username = authenticate_form.cleaned_data.get('username')
            password = authenticate_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                print('User not found')
        else:
            return render(request, 'accounts/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    return render(request, template_name='accounts/signup.html')
