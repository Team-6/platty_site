from django.test import TestCase, Client
from django.contrib.auth.models import User
from datetime import datetime
from platty.models import *

# Create your tests here.
class EventTestCase(TestCase):
    def setUp(self):
        Event.objects.create(name="party1", date_time=datetime.now(), zipCode=84352)
        Event.objects.create(name="party2", date_time=datetime.now(), zipCode=84334)
    
    def test_event(self):
        p1 = Event.objects.get(name="party1")
        p2 = Event.objects.get(name="party2")

        self.assertEqual(p1.zipCode, 84352)
        self.assertEqual(p2.zipCode, 84334)

    def test_create_event_from_post(self):
        c = Client()
        response = c.post('/signup/', { 'username' : 'muffin', 
                                        'email' : 'myemail@email.com',
                                        'password' : 'password',
                                        'firstName' : 'Eric',
                                        'lastName' : 'Muffin', } )
        response.status_code
        self.assertEqual(response.status_code, 200)
