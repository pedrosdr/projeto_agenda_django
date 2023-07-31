from django.http import HttpRequest
from django.shortcuts import render
from contact.forms import RegisterForm


def register(request: HttpRequest):
    form = RegisterForm()

    if request.method.upper() == 'POST':
        form = RegisterForm(request.POST)
        form.save()

    return render(
        request,
        'contact/register.html',
        {'form': form}
    )