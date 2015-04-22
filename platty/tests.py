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

    def test_event_create(self):
        
        #todo how do I set user to be active?

        c = Client()

        
        #create and login the user
        username = "muffin"
        password = "themuffinman"
        email = "muffinman@gmail.com"
        User.objects.create_user(
            username,
            email,
            password,
            first_name = "Eric",
            last_name = "Muffin",
        )

        user = authenticate(username=username, password=password)
        user.is_active = True

        #make a create request with valid information. clicked the button
        response = c.post('/create/', { 'user' : user,
                                        'verified' : 'yes',
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
        self.assertEqual(response.redirect_chain[0], "http://localhost::8000/parties/")
        self.assertEqual(muffinParty.name, "The Muffin Man")

