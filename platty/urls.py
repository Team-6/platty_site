from django.conf.urls import url

from . import views

#admin.autodiscover()

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^create/$', views.create, name='create'),
    url(r'^edit/(?P<event_id>[0-9]+)$', views.edit, name='edit'),
    url(r'^find/$', views.find, name='find'),
    url(r'^parties/$', views.parties, name='parties'),
    url(r'^login/$', views.login, name='login'),
    url(r'^profile/$', views.profile, name='profile'), 
]
