from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
            messages.info(request, f"You are now logged in as {user.username}")
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password.")

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
                user = signup_form.save()

                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request, f"New account created and logged in successfully: {user.username}")
                return redirect('/')
            else:
                for msg in signup_form.error_messages:
                    messages.error(request, f"{msg}: {signup_form.error_messages[msg]}")

        return render(request, template_name='accounts/signup.html')

    return redirect('/')
