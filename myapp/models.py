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

class User_detail(models.Model):
    user_detail_name=models.CharField(max_length=100)
    user_detail_email=models.CharField(max_length=100)
    user_detail_password=models.CharField(max_length=100)
    def __str__(self):
        return self.user_detail_name
    
class Blog(models.Model):
    title=models.TextField()
    description=models.TextField()
    author=models.ForeignKey(User_detail, on_delete=models.CASCADE)
    date=today_date = timezone.now().date()

class Chat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} -> {self.recipient}: {self.content}'



# Create your models here.
