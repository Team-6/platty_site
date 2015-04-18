from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.db import models
from datetime import datetime
from .models import Event
from .forms import EventForm

def index(request):
        return HttpResponse('Hey there, you are at the home index!')
# Create your views here.

def home(request):
    return render(request, 'platty/index.html', {})

def create(request):
    event = Event(date_time = datetime.now(), zipCode="0")
    event.save()
    return HttpResponseRedirect(reverse('platty:edit', args=(event.id,)))

def edit(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.POST:
        name = request.POST.get('partyName', '')
        event.name.set(name)
        desc = request.POST.get('desc', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        pZipCode = request.POST.get('zipCode', '')
        print pZipCode

    return render(request, 'platty/create.html', {'event': event})


def parties(request):
    return render_to_response('platty/parties.html', context_instance=RequestContext(request))

def find(request):
    return render_to_response('platty/find.html', context_instance=RequestContext(request))

def login(request):
    return render_to_response('platty/login.html', context_instance=RequestContext(request))

def profile(request):
    return render_to_response('platty/profile.html', context_instance=RequestContext(request))
