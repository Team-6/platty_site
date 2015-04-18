from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext, loader

from django.db import models
from datetime import datetime
from .models import Event

def index(request):
        return HttpResponse('Hey there, you are at the home index!')
# Create your views here.

def home(request):
    return render(request, 'platty/index.html', {})

def create(request):
    #name = request.POST['partyName']
    event = Event(date_time = datetime.now(), name="fdasfs", description="fdsafdsa", zipCode="84720",)
    event_list = Event.objects.order_by('-id')[:5]
    template = loader.get_template('platty/create.html')
    context = RequestContext(request, {
        'event_list': event_list,
    })
    event.save()
    return HttpResponse(template.render(context))

def saveParty(request, event):
    print 'a'
    #return HttpResponseRedirect(reverse('platty/create.html'))

def parties(request):
    return render_to_response('platty/parties.html', context_instance=RequestContext(request))

def find(request):
    return render_to_response('platty/find.html', context_instance=RequestContext(request))

def login(request):
    return render_to_response('platty/login.html', context_instance=RequestContext(request))

def profile(request):
    return render_to_response('platty/profile.html', context_instance=RequestContext(request))
