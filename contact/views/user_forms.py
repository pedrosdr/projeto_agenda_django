from django.http import HttpRequest
from django.shortcuts import render, redirect
from contact.forms import RegisterForm
from django.contrib import messages


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
        {'form': form}
    )