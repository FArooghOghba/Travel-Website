from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from accounts.forms import CustomUserCreationForm, CustomAuthenticationForm


# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'POST':
        authenticate_form = CustomAuthenticationForm(request=request, data=request.POST)

        if authenticate_form.is_valid():
            user = authenticate_form.get_user()
            login(request, user)
            return redirect('/')

    return render(request, 'accounts/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            signup_form = CustomUserCreationForm(request.POST)
            if signup_form.is_valid():
                signup_form.save()
                return redirect(reverse('accounts:login'))
        return render(request, template_name='accounts/signup.html')

    return redirect('/')
