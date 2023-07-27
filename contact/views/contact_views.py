from django.shortcuts import render, redirect
from django.http import HttpRequest, Http404
from contact.models import Contact
from django.db.models import Q

def index(request: HttpRequest):
    contacts = Contact.objects\
        .filter(show=True)\
        .order_by('-id')[20:30]

    context = {
        'contacts': contacts,
        'page_title': 'Agenda'
    }

    return render(request, 'contact/index.html', context)


def contact(request: HttpRequest, contact_id: int):
    # contact = Contact.objects.get(pk=contact_id)
    contact = Contact.objects.filter(pk=contact_id, show=True).first()

    if contact is None:
        raise Http404('Contact not found')

    context = {
        'contact': contact,
        'page_title': 'Contact - ' + contact.first_name
    }

    return render(request, 'contact/contact.html', context)

def search(request: HttpRequest):
    # search_value = request.GET['q']
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects\
        .filter(show=True)\
        .filter(Q(first_name__icontains=search_value) | Q(last_name__icontains=search_value))\
        .order_by('-id')

    context = {
        'contacts': contacts,
        'page_title': 'Agenda'
    }

    return render(request, 'contact/index.html', context)