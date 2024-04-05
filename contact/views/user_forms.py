from django.http import HttpRequest
from django.shortcuts import render, redirect
from contact.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


def register(request: HttpRequest):
    form = RegisterForm()

    if request.method.upper() == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'User succesfully registered')
            return redirect('contact:register')

        return render(
            request,
            'contact/register.html',
            {'form': form}
        )

    return render(
        request,
        'contact/register.html',
        {
            'form': form,
            'messages': messages.get_messages(request)
         }
    )


def login_view(request: HttpRequest):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            print(user)
        else:
            messages.error(request, 'Login inválido')

    return render(
        request,
        'contact/login.html',
        {
            'form': form
        }
    )

def logout_view(request: HttpRequest):
    auth.logout(request)
    return redirect('contact:login')