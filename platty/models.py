from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
	date_time = models.DateTimeField(blank=True)
	name = models.CharField(max_length=64, blank=True)
	addressLineOne = models.CharField(max_length=128, blank=True)
	addressLineTwo = models.CharField(max_length=128, blank=True)
	city = models.CharField(max_length=36, blank=True)
	state = models.CharField(max_length=2, blank=True)
	zipCode = models.PositiveIntegerField(max_length=5, blank=True)
	description = models.CharField(max_length=1024, blank=True)
	id = models.AutoField(primary_key=True)

class Role(models.Model):
	user = models.ForeignKey(User)
	event = models.ForeignKey(Event)
	OWNER = 0
	GOER = 1
	ROLE_CHOICES = (
			(OWNER, 'Owner'),
			(GOER, 'Goer'),
	)
	role = models.IntegerField(max_length=1,
								choices=ROLE_CHOICES,
								default=GOER)

class Requirement(models.Model):
	event = models.ForeignKey(Event)
	description = models.CharField(max_length=256)
	quanitity = models.IntegerField(max_length=11)
	id = models.AutoField(primary_key=True)

class Contribution(models.Model):
	user = models.ForeignKey(User)
	event = models.ForeignKey(Event)
	requirement = models.ForeignKey(Requirement)
	value = models.IntegerField(max_length=11)

class Donation(models.Model):
	user = models.ForeignKey(User)
	event = models.ForeignKey(Event)
	value = models.DecimalField(max_digits=11, decimal_places=2)
