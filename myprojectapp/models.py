from django.db import models
from django.db import models
import email
from operator import mod
import uuid
from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone

from datetime import datetime
from django.utils import timezone

class Room(models.Model):
    name = models.CharField(max_length=255)
class Eitheruserlawyer(models.Model):
    type=models.CharField(max_length=100)
class User_detail(models.Model):
    eitheruserlawyer = models.ForeignKey(Eitheruserlawyer, default=1,on_delete=models.CASCADE)
    user_detail_name = models.CharField(max_length=100)
    user_detail_email = models.CharField(max_length=100)
    type = models.CharField(default='user', editable=False, max_length=100)
    user_detail_password = models.CharField(max_length=100)

    def __str__(self):
        return self.user_detail_name
    
class Extradetaillawer(models.Model):
    catagory=models.CharField(max_length=100,default="N/A")
    contact=models.CharField(max_length=100,default="N/A")
    country=models.CharField(max_length=100,default="N/A")
class Laweruser(models.Model):
    eitheruserlawyer = models.ForeignKey(Eitheruserlawyer,default=1, on_delete=models.CASCADE)
    extradetaillawer=models.ForeignKey(Extradetaillawer,default=1, on_delete=models.CASCADE)
    room=models.ForeignKey(Room,default=1,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    type = models.CharField(default='lawer', editable=False, max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

    


class Blog(models.Model):
    title=models.TextField()
    description=models.TextField()
    author=models.ForeignKey(User_detail, on_delete=models.CASCADE)
    date=today_date = timezone.now().date()
    def __str__(self):
        return self.title

class Lawyer(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    catagory=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Chat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(Lawyer, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} -> {self.recipient}: {self.content}'

class Typelawer(models.Model):
    laweruser=models.ForeignKey(Laweruser,default=1,on_delete=models.CASCADE)
    type=models.TextField(default="Criminals laweyers")


class ChatRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
    receiver = models.ForeignKey(Extradetaillawer, on_delete=models.CASCADE, related_name='received_requests')
    accepted = models.BooleanField(default=False)





class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)


class Advocatecatagory(models.Model):
    cat=models.TextField(default="N/A")

class Advocate(models.Model):
    name = models.CharField(max_length=255, default='N/A')  # Default name is 'N/A'
    location = models.CharField(max_length=255, default='N/A')  # Default location is 'N/A'
    experience = models.CharField(max_length=255, default='N/A')  # Default experience is 'N/A'
    type = models.CharField(max_length=100, default='Other')  # Default type is 'Other'
    rating = models.CharField(max_length=100, default='N/A')  # Default rating is 'N/A'
    image_url = models.URLField(default='https://example.com/default-image.jpg')  # Default image URL

    def __str__(self):
        return self.name

# Create your models here.
