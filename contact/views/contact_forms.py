from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpRequest
from contact.forms import ContactForm


def create(request: HttpRequest):
    if request.method.upper() == 'POST':
        context = {
            'form': ContactForm(request.POST)
        }

        return render(
        request,
        'contact/create.html',
        context
    )

    context = {
        'form': ContactForm()
    }

    return render(
        request,
        'contact/create.html',
        context
    )