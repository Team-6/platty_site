from django.conf.urls import url

from . import views

#admin.autodiscover()

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^create/$', views.create, name='create'),
    url(r'^find/$', views.find, name='find'),
    url(r'^parties/$', views.parties, name='parties'),
    url(r'^parties/(\d+)/$', views.party, name='parties'),
    url(r'^login/$', views.login_page, name='login'),
    url(r'^logout/$', views.logout_page, name='logout'),
    url(r'^profile/$', views.profile, name='profile'), 
]
