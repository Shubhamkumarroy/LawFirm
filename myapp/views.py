from django.shortcuts import render,HttpResponse
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os,sys
import subprocess
import threading,time
import base64
from django.contrib.auth.decorators import login_required
from audioop import reverse
from cmath import log
import email
import time
from re import template
import re
from datetime import datetime
from unittest import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date,datetime
from django.db import IntegrityError
from django.utils import timezone
from django.db.models import Q


# Create your views here.
def accountcreate(request):
    return render (request,'signup.html')

def check_login(request):
        # {% if user.is_authenticated %}  this can be used in frontend
        user=request.user
        # good to know this that fn exist for authentication
        if user.is_authenticated:  
            return True
        else :
            return False
       
@csrf_exempt
def signup(request):
    if request.method == "POST":
        try:
            username = request.POST['username']
            firstname = request.POST['fname']
            lastname = request.POST['lname']
            email = request.POST['email']
            pass1 = request.POST['password']
            myuser = User.objects.create_user(username, email, pass1)
            user_db = User_detail(user_detail_name=username, user_detail_email=email, user_detail_password=pass1)
            myuser.first_name = firstname
            myuser.last_name = lastname
            myuser.save()
            user_db.save()
            user = authenticate(username=username, password=pass1)
            user_status = 1
            user_d = request.user
            obj = Blog.objects.all()
            context = {
                'obj': obj,
                "user_d": user_d,
                "user_status": user_status
            }
            
            if user is not None:
                login(request, user)
                id1 = user.id
                return render(request, 'index.html', context)
            else:
                return render(request, 'loginpage.html')
        except IntegrityError:
            error_message = "Username or email already taken. Please choose a different username or email."
            return render(request, 'signup.html', {'error_message': error_message})
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return render(request, 'error_page.html', {'error_message': error_message})
    else:
        return render(request, 'signup.html')
    
@csrf_exempt
def loginuser(request):
    if request.method == "POST":
        try:
            user_d = request.user
            username = request.POST['username']
            pass1 = request.POST['password']
            
            user = authenticate(username=username, password=pass1)
            
            if user is not None:
                login(request, user)
                id1 = user.id
                user_status = 1
                obj = Blog.objects.all()
                context = {
                    'obj': obj,
                    'user_d': user_d,
                    'user_status': user_status
                }
                return render(request, 'index.html', context)
            else:
                error_message = "Invalid username or password."
                return render(request, 'loginpage.html', {'error_message': error_message})
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return render(request, 'error_page.html', {'error_message': error_message})
    else:
        return render(request, 'loginpage.html')

@csrf_exempt
def logoutuser(request):
    try:
        logout(request)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'error_page.html', {'error_message': error_message})
    
    return render(request, 'loginpage.html')
@csrf_exempt
def index(request):
    # return render(request,'dummyblog.html')
    if request.user.is_authenticated:
        context={
           
        }
        return render(request,'carousel.html',context)
    else :
        return render(request,'signup.html')

@csrf_exempt
def carousel(request):
    if request.user.is_authenticated:
        context={
           
        }
        return render(request,'carousel.html',context)
    else :
        return render(request,'signup.html')

def blog(request):
    if request.method=="GET":
        obj=Blog.objects.all()
        print(obj)
        context={
            'obj':obj
        }
        return render(request,'blog.html',context)
    
    
def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "chatage.html", context)

def chat_with_user(request, recipient_username):
    return render(request, 'chatpage.html', {
        'recipient_username': recipient_username})
def chat(request,id1,id2):
    user1=User.objects.filter(pk=id1)
    user2=User.objects.filter(pk=id2)
    if request.method=="POST":
        content=request.POST['message']
        chat=Chat(sender=user1[0],recipient=user2[0],content=content)
        chat.save()
    chat_history = Chat.objects.filter(Q(sender=user1[0], recipient=user2[0]) | Q(sender=user2[0], recipient=user1[0])).order_by('timestamp')
    context={
        'u1':user1[0],
        'u2':user2[0],
        "chat_history":chat_history
    }
    return render(request,'chatpage.html',context)

def readmore(request,id1):
    if request.method=="GET":
        obj=Blog.objects.filter(pk=id1)
        context={
            'obj':obj[0]
        }
        return render(request,'blogafteropen.html',context)



