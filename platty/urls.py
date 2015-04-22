from django.conf.urls import url
from django.contrib.auth.views import password_change

from . import views

#admin.autodiscover()

urlpatterns = [
    url(r'^$', views.parties, name='home'),
    url(r'^create/$', views.create, name='create'),
    url(r'^find/$', views.find, name='find'),
    url(r'^parties/$', views.parties, name='parties'),
    url(r'^parties/(\d+)/$', views.party, name='parties'),
    url(r'^edit/(?P<party_id>[0-9]+)/$', views.edit, name='edit'),
    url(r'^edit/(?P<party_id>[0-9]+)/submit/$', views.submit, name='submit'),
    url(r'^login/$', views.login_page, name='login'),
    url(r'^logout/$', views.logout_page, name='logout'),
    url(r'^profile/$', views.profile, name='profile'), 
    url(r'^signup/$', views.signup, name='signup'), 
]
