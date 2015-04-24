from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.auth import *
from datetime import datetime
from platty.models import *

# Create your tests here.
class EventTestCase(TestCase):
    def setUp(self):
        Event.objects.create(name="party1", date_time=datetime.now(), zipCode=84352)
        Event.objects.create(name="party2", date_time=datetime.now(), zipCode=84334)
        self.c = Client()
        
        self.username = "muffin"
        self.password = "muffinman"
        self.email = "muffinman@gmail.com"
        User.objects.create_user(
            self.username,
            self.email,
            self.password,
            first_name = "Eric",
            last_name = "Muffin",
        )

        response = self.c.post('/login/', {
            'username' : "muffin",
            'password' : "muffinman",})

    def test_event(self):
        p1 = Event.objects.get(name="party1")
        p2 = Event.objects.get(name="party2")

        self.assertEqual(p1.zipCode, 84352)
        self.assertEqual(p2.zipCode, 84334)

    def test_signup(self):

        #submitButtonClicked information given, redirected to login page.
        response = self.c.post('/signup/', { 'submit' : 'submit',
                                        'username' : 'muffinman', 
                                        'email' : 'myemail@email.com',
                                        'password' : 'password',
                                        'firstName' : 'Eric',
                                        'lastName' : 'Muffin', }, follow=True )
        self.assertEqual(len(response.redirect_chain), 1)
        
    def test_event_create(self):
        
        #todo how do I set user to be active?
        
        #create and login the user

        user = authenticate(username=self.username, password=self.password)
        user.is_active = True

        #make a create request with valid information. clicked the button
        response = self.c.post('/create/', { 'verified' : 'yes',
                                        'submit' : 'submit',
                                        'name' : 'The Muffin Man', 
                                        'description' : 'The Muffin Man?',
                                        'date' : '2000-07-15',
                                        'time' : '15:32',
                                        'address1' : 'Drury Lane',
                                        'address2' : '666',
                                        'city' : 'Bakersville',
                                        'state' : 'THE MUFFIN MAN',
                                        'zip' : '84357', }, follow=True )
        muffinParty = Event.objects.get(name="The Muffin Man")
        
        self.assertEqual(len(response.redirect_chain), 1)
        self.assertEqual(response.redirect_chain[0][0], "http://testserver/parties/")
        self.assertEqual(muffinParty.name, "The Muffin Man")

