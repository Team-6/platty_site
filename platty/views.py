from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.db import models
from datetime import datetime
from .models import *

def index(request):
        return HttpResponse('Hey there, you are at the home index!')
# Create your views here.

def home(request):
    if request.user.is_active:
        template = loader.get_template('platty/index.html')
        context = RequestContext(request, {
            'selected_page': 'home',
            'context_instance': request
        })
        return HttpResponse(template.render(context))
    else:
        return redirect('/login/')

def create(request):
    if request.user.is_active:
        if 'submit' not in request.POST:
            template = loader.get_template('platty/create.html')
            context = RequestContext(request, {
                'context_instance': request
            })
            return HttpResponse(template.render(context))
        else:
            new_event = Event(
                name=request.POST['name'],
                description=request.POST['description'],
                date_time=request.POST['date'] + ' ' + request.POST['time'],
                addressLineOne=request.POST['address1'],
                addressLineTwo=request.POST['address2'],
                city=request.POST['city'],
                state=request.POST['state'],
                zipCode=request.POST['zip']
            )
            new_event.save()
            role = Role(
                user = request.user,
                event = new_event,
                role=0
            )
            role.save()
            return redirect('/parties/')                
    else:
        return redirect('/login/')

def parties(request):
    if request.user.is_active:
        hosting_list = Event.objects.filter(role__user=request.user.id, role__role=0).order_by('-name')
        going_list = Event.objects.filter(role__user=request.user.id, role__role=1).order_by('-name')
        template = loader.get_template('platty/parties.html')
        context = RequestContext(request, {
            'hosting_list': hosting_list,
            'going_list': going_list,
            'context_instance': request
        })
        return HttpResponse(template.render(context))
    else:
        return redirect('/login/')

def party(request, party_id):
    return render_to_response('platty/parties.html', context_instance=RequestContext(request))

def find(request):
    if request.user.is_active:
        template = loader.get_template('platty/find.html')

        searchedFor = request.GET.get('keywords', '')
        event_list = Event.objects.filter(name__icontains=searchedFor)

        context = RequestContext(request, {
            'event_list': event_list,
            'searched_for': searchedFor,
            'context_instance': request
        })

        return HttpResponse(template.render(context))
    else:
        return redirect('/login/')

def login_page(request):
    if 'username' not in request.POST:
	    return render_to_response('platty/login.html', context_instance=RequestContext(request))

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/')
            # Redirect to a success page.
        else:
            x = 5
            # Return a 'disabled account' error message
    else:
        x = 5
        # Return an 'invalid login' error message.
    return render_to_response('platty/login.html', context_instance=RequestContext(request))
    
def logout_page(request):
    logout(request)
    return redirect('/login/')

def profile(request):
    if request.user.is_active:
        return render_to_response('platty/profile.html', context_instance=RequestContext(request))
    else:
        return redirect('/login/')

def signup(request):
    if 'submit' not in request.POST:
        return render_to_response('platty/signup.html', context_instance=RequestContext(request))
    else:
        User.objects.create_user(
            request.POST['username'],
            request.POST['email'],
            request.POST['password'],
            first_name = request.POST['firstName'],
            last_name = request.POST['lastName'],
        )
        return redirect('/login/')
