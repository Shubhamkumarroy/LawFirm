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
import requests
from bs4 import BeautifulSoup

# Create your views here.
def storedata(request):
    # return render(request,'navebar.html')
    list1=[]
    list1.append("arbitration-lawyers")
    list1.append("anticipatory-bail-lawyers")
    list1.append("banking-finance-lawyers")
    list1.append("bankruptcy-insolvency-lawyers")
    list1.append("breach-of-contract-lawyers")
    list1.append("civil-lawyers")
    list1.append("corporate-lawyers")
    list1.append("family-lawyers")
    list1.append("criminal-lawyers")
    list1.append("cyber-crime-lawyers")
    list1.append("domestic-violence-lawyers")
    list1.append("divorce-lawyers")
    list1.append("muslim-law-lawyers")
    cnt=0
    for l1 in list1:
        # URL of the page for the current advocate type
        url = f'https://lawrato.com/{l1}'
        cnt+=1
        
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all the lawyer listings with the specified class
            lawyer_listings = soup.find_all('div', class_='lawyer-item border-box')

            # Loop through all the lawyer listings for the current advocate type
            for lawyer in lawyer_listings:
                # Extract lawyer's name
                name = lawyer.find('h2', class_='media-heading').text.strip()

                # Extract lawyer's location
                location = lawyer.find('div', class_='location').text.strip()

                # Extract lawyer's experience
                experience = lawyer.find('div', class_='experience').text.strip()
                image_url = lawyer.find('img', class_='media-object')['src']
                # areaskill=lawyer.find('div', class_='area-skill').text.strip()

                # Extract lawyer's contact link
                # contact_link = lawyer.find('a', title='CONTACT NOW')['href']

                # Extract lawyer's rating
                rating = lawyer.find('span', class_='score').text.strip()
                advocate = Advocate(
                name=name,
                type=l1,
                location=location,
                experience=experience,
                rating=rating,
                image_url=image_url
                )
                cat=Advocatecatagory(cat=l1)
                cat.save()
                advocate.save()

                # Print or store the extracted information for each lawyer
                print(f"Type: {l1}")
                print(f"Name: {name}")
                print(f"Location: {location}")
                print(f"Experience: {experience}")
                # print(f"Contact Link: {contact_link}")
                print(f"Rating: {rating}")
                print()
        else:
            print(f"Failed to retrieve the page for {l1}. Status code:", response.status_code)

    return render(request,'navebar.html')
def accountcreate(request):
        try:
            return render(request, 'signup.html')
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return render(request, 'error_page.html', {'error_message': error_message})

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
            type=Eitheruserlawyer(type="user")
            type.save()
            myuser = User.objects.create_user(username, email, pass1)
            user_db = User_detail(eitheruserlawyer=type,user_detail_name=username, user_detail_email=email, user_detail_password=pass1)
            myuser.first_name = firstname
            myuser.last_name = lastname
            myuser.save()
            user_db.save()
            user = authenticate(username=username, password=pass1)
            user_status = 1
            user_d = request.user
            obj = Blog.objects.all()
            lawyer=Laweruser.objects.all()
            # # # lawyer=Lawyer.objects.all()
            context = {
                'obj': obj,
                "user_d": user_d,
                "user_status": user_status,
                'lawyer':lawyer
            }
            
            if user is not None:
                login(request, user)
                id1 = user.id
               
                return render(request, 'index2.html', context)
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
def signuplawyer(request):
    if request.method == "POST":
        try:
            username = request.POST['username']
            firstname = request.POST['fname']
            lastname = request.POST['lname']
            email = request.POST['email']
            pass1 = request.POST['password']
            type=Eitheruserlawyer(type="lawyer")
            type.save()
            myuser = User.objects.create_user(username, email, pass1)
            user_db = User_detail(eitheruserlawyer=type,user_detail_name=username, user_detail_email=email, user_detail_password=pass1)
            myuser.first_name = firstname
            myuser.last_name = lastname
            extradetaillawer=Extradetaillawer.objects.filter(pk=1)
            laweruser=Laweruser(eitheruserlawyer=type,extradetaillawer=extradetaillawer[0],name=username,fname=firstname,lname=lastname,email=email, password=pass1)
            myuser.save()
            user_db.save()
            laweruser.save()
            typelawyer=Typelawer(laweruser=laweruser)
            typelawyer.save()
            user = authenticate(username=username, password=pass1)
            user_status = 1
            user_d = request.user
            obj = Blog.objects.all()
            # # lawyer=Lawyer.objects.all()
            lawyer=Laweruser.objects.all()
            context = {
                'obj': obj,
                "user_d": user_d,
                "user_status": user_status,
                #  'lawyer':lawyer,
                'lawyer':lawyer
            }
            
            if user is not None:
                login(request, user)
                id1 = user.id
               
                return render(request, 'index2.html', context)
            else:
                return render(request, 'loginpage.html')
        except IntegrityError:
            error_message = "Username or email already taken. Please choose a different username or email."
            return render(request, 'signuplawer.html', {'error_message': error_message})
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return render(request, 'error_page.html', {'error_message': error_message})
    else:
        return render(request, 'signuplawer.html')

    
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
                # # lawyer=Lawyer.objects.all()
                lawyer=Laweruser.objects.all()
                print(lawyer)
                context = {
                    'obj': obj,
                    'user_d': user_d,
                    'user_status': user_status,
                    #  'lawyer':lawyer,
                    'lawyer':lawyer
                }

                return render(request, 'index2.html', context)
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
        # # lawyer=Lawyer.objects.all()
        lawyer=Laweruser.objects.all()
        logout(request)
        context = {
            #  'lawyer':lawyer,
            'lawyer':lawyer
        }
        return render(request, 'index2.html',context)
        
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'error_page.html', {'error_message': error_message})
    
    return render(request, 'loginpage.html')
@csrf_exempt
def index(request):
    # return render(request,'dummychat.html')
    # # lawyer=Lawyer.objects.all()
    lawyer=Laweruser.objects.all()
    # logout(request)
    context = {
        #  'lawyer':lawyer,
        'lawyer':lawyer
    }
    return render(request, 'index2.html',context)
    try:
        if request.user.is_authenticated:
            context = {}
            return render(request, 'index2.html', context)
        else:
            return render(request, 'signup.html')
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'error_page.html', {'error_message': error_message})
    
@csrf_exempt
def home(request):
    # # lawyer=Lawyer.objects.all()
    lawyer=Laweruser.objects.all()
    # logout(request)
    context = {
        #  'lawyer':lawyer,
        'lawyer':lawyer
    }
    # print
    return render(request, 'index2.html',context)

@csrf_exempt
def carousel(request):
    try:
        if request.user.is_authenticated:
            context = {}
            return render(request, 'carousel.html', context)
        else:
            return render(request, 'signup.html')
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'error_page.html', {'error_message': error_message})

def blog(request):
    try:
        if request.method == "GET":
            obj = Blog.objects.all()
            context = {'obj': obj}
            return render(request, 'blog.html', context)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'error_page.html', {'error_message': error_message})
    


def chatPage(request, *args, **kwargs):
    try:
        if not request.user.is_authenticated:
            return redirect("login-user")
        
        context = {}
        return render(request, "chatage.html", context)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'error_page.html', {'error_message': error_message})

def chat_with_user(request, recipient_username):
    return render(request, 'chatpage.html', {
        'recipient_username': recipient_username})

@csrf_exempt
def chat(request,receiver_id):
    if request.method == "POST":
        return 
    else : 
        chat_request = ChatRequest.objects.get(pk=receiver_id)



    
    
    


def readmore(request, id1):
    try:
        if request.method == "GET":
            obj = Blog.objects.filter(pk=id1)
            context = {
                'obj': obj[0]
            }
            return render(request, 'blogafteropen.html', context)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'error_page.html', {'error_message': error_message})

def dashboard(request):
    try:
        # print(request.user.username)
        # user=User_detail.objects.filter(pk=request.user.id)
        # print(user)
        # return render(request,'navebar.html')
        return render(request, 'profile.html')
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'error_page.html', {'error_message': error_message})

def setting(request):
    try:
        return render(request, 'profile.html')
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'error_page.html', {'error_message': error_message})
    
def lawyer(request,id1):
    try:
        # return render(request,'navebar.html')
        lawyer=Laweruser.objects.filter(pk=id1)
        
        context={
            'lawyer':lawyer[0],
        }
        print(lawyer)
        # return render(request,'navebar.html')
       
        
        return render(request, 'lawyer.html',context)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'error_page.html', {'error_message': error_message})
    
def send_chat_request(request,receiver_id):
    try:
        receiver = Extradetaillawer.objects.get(pk=receiver_id)
        chat_request=ChatRequest(sender=request.user,receiver=receiver)
        chat_request.save()
        messages.success(request, 'abhi accept nhi hua hai')
        lawyer=Extradetaillawer.objects.filter(pk=receiver_id)
        print(lawyer)
        chatrequest=ChatRequest.objects.filter(receiver=lawyer[0])
        cnt=len(chatrequest)
        print(cnt)
        context={
            'lawyer':lawyer[0],
            'cnt':cnt
        }
        if cnt!=0:
            context['chatrequest']=chatrequest[0]
        print(context)
        # return render(request,'navebar.html')
        return render(request, 'lawyer.html',context)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'error_page.html', {'error_message': error_message})


def accept_chat_request(request, request_id):
    chat_request = ChatRequest.objects.get(pk=request_id)
    chat_request.accepted = True
    chat_request.save()
    return redirect('chat', chat_request.receiver.id)


@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, id1,id2):
    room = Room.objects.get(pk=id2)
    lawyer=Laweruser.objects.filter(pk=id1)
    print(lawyer)
    room=lawyer[0].room
    messages = Message.objects.filter(room=room)[0:25]
    
        
    context={
        'lawyer':lawyer[0],
        'messages':messages
    }
        
        # return render(request,'navebar.html')
       
        
    return render(request, 'room.html',context)

    # return render(request, 'room.html', {'room': room, 'messages': messages})

def typelawyer(request,type):
    type=Typelawer.objects.filter(type=type)
    cnt=len(type)
    context={
        'type':type,
        'cnt':cnt
    }
    
    return render(request,'filteradvocate.html',context)

def update(request,id1):
    try:
        pass
        user=request.user
        # user
    except:
        pass

def consult(request):
    return render(request,'problem.html')

def submitproblem(request):
    if request.method == "post":
        city=request.post['city']
        problem=request.post['problem']

    return render(request,'navebar.html')

def advocates_by_type(request, advocate_type):
    advocates = Advocate.objects.filter(type=advocate_type)
    return render(request, 'lawyerCard.html', {'Lawyers': advocates})


    
    






