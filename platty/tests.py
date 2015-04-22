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

    def test_signup(self):
        c = Client()

        #submitButtonClicked information given, redirected to login page.
        response = c.post('/signup/', { 'submit' : 'submit',
                                        'username' : 'muffin', 
                                        'email' : 'myemail@email.com',
                                        'password' : 'password',
                                        'firstName' : 'Eric',
                                        'lastName' : 'Muffin', }, follow=True )
        
        user = User.objects.get(email="myemail@email.com")
        self.assertEqual(len(response.redirect_chain), 1)
        self.assertEqual(user.email, "myemail@email.com")
        
        response = c.post('/signup/', { 
                                        'username' : 'muffin', 
                                        'email' : 'myemail@email.com',
                                        'password' : 'password',
                                        'firstName' : 'Eric',
                                        'lastName' : 'Muffin', }, follow=True )
        
        #same. submit button not clicked
        self.assertEqual(len(response.redirect_chain), 0)
