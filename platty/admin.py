from django.contrib import admin

from .models import Event, Role, Requirement, Contribution, Donation

# Register your models here.
admin.site.register(Event)
admin.site.register(Role)
admin.site.register(Requirement)
admin.site.register(Contribution)
admin.site.register(Donation)
