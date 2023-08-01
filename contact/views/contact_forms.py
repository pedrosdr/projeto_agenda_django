from typing import Any, Dict
from django.shortcuts import render, redirect
from django.http import HttpRequest
from contact.forms import ContactForm
from django.urls import reverse
from contact.models import Contact


def create(request: HttpRequest):
    form_action = reverse('contact:create')

    if request.method.upper() == 'POST':
        form = ContactForm(request.POST, request.FILES)

        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            contact = form.save()
            return redirect('contact:contact', contact_id=contact.pk)

        return render(
        request,
        'contact/create.html',
        context
    )

    context = {
        'form': ContactForm(),
        'form_action': form_action
    }

    return render(
        request,
        'contact/create.html',
        context
    )


def update(request: HttpRequest, contact_id: int):
    form_action = reverse('contact:update', args=(contact_id,))
    
    contact = Contact.objects.filter(pk=contact_id, show=True).first()

    if request.method.upper() == 'POST':
        print('valid')
        form = ContactForm(request.POST, request.FILES, instance=contact)
        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            contact = form.save()
            return redirect('contact:contact', contact_id)
        
        return render(
            request,
            'contact/create.html',
            context
        )
    
    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action
    }

    return render(
        request,
        'contact/create.html',
        context
    )


def delete(request: HttpRequest, contact_id: int):
    contact = Contact.objects.filter(pk=contact_id, show=True).first()
    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'confirmation': confirmation
        }
    )


def login_view(request: HttpRequest):
    return render(
        request,
        'contact/login.html',
        {
            'form': 'form'
        }
    )