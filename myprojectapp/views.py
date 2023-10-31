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
import openai
from django.db.models import Subquery
# from your_app.models import UserProfilePhoto


def get_gpt3_response(user_message):
    api_key = os.environ.get('BOTAPIKEY')
    

    # # print(api_key)
    openai.api_key = api_key
    # Create a conversation prompt
    conversation_history = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_message}
    ]

    # Convert conversation history to GPT-3.5 input format
    prompt = "\n".join(f"{item['role']}: {item['content']}" for item in conversation_history)

    # Get GPT-3.5 response
    response = openai.Completion.create(
        engine="text-davinci-002",  # GPT-3.5 engine
        prompt=prompt,
        max_tokens=150  # Adjust as needed
    )

    gpt3_response = response.choices[0].text.strip()
    return gpt3_response

# Example usage

def fn(request):
    #str="Choose from Given options what type of lawyer i need.and option are "
    str = "Reply in one word from given options what type of lawyer i need and options are "
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
    list1.append("wills-trusts-lawyers")
    list1.append("copyright-patent-trademark-lawyers")
    list1.append("court-marriage-lawyers")
    list1.append("domestic-violence-lawyers")
    list1.append("gst-lawyers")
    list1.append("immigration-lawyers")
    list1.append("labour-service-lawyers")
    list1.append("media-entertainment-lawyers")
    list1.append("medical-negligence-lawyers")
    cnt=0
    sz=len(list1)
    for l1 in list1:
        str +=l1
        str +=" ,"

   # str +="I need reply in one word and exact same to given option with hyphen."  
    return str

def lawerexactmatch(request):
    list1=[]
    list1.append("arbitration")
    list1.append("anticipatory")
    list1.append("banking")
    list1.append("bankruptcy")
    list1.append("breach")
    list1.append("civil")
    list1.append("corporate")
    list1.append("family")
    list1.append("criminal")
    list1.append("cyber")
    list1.append("domestic")
    list1.append("divorce")
    list1.append("muslim")
    list1.append("wills")
    list1.append("copyright")
    list1.append("court")
    list1.append("domestic")
    list1.append("gst")
    list1.append("immigration")
    list1.append("labour")
    list1.append("media")
    list1.append("medical")
    return list1
def lawerecatagoryexactmatch(request):
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
    list1.append("wills-trusts-lawyers")
    list1.append("copyright-patent-trademark-lawyers")
    list1.append("court-marriage-lawyers")
    list1.append("domestic-violence-lawyers")
    list1.append("gst-lawyers")
    list1.append("immigration-lawyers")
    list1.append("labour-service-lawyers")
    list1.append("media-entertainment-lawyers")
    list1.append("medical-negligence-lawyers")
    return list1






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
                print(name)
                cat=Advocatecatagory(cat=l1)
                cat.save()
                advocate.save()

                # # print or store the extracted information for each lawyer
                # print(f"Type: {l1}")
                # print(f"Name: {name}")
                # print(f"Location: {location}")
                # print(f"Experience: {experience}")
                # # print(f"Contact Link: {contact_link}")
                # print(f"Rating: {rating}")
                # print()
        else:
            print(f"Failed to retrieve the page for {l1}. Status code:", response.status_code)

    return render(request,'navebar.html')



def webscrapdata(request):
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
    list1.append("wills-trusts-lawyers")
    list1.append("copyright-patent-trademark-lawyers")
    list1.append("court-marriage-lawyers")
    list1.append("domestic-violence-lawyers")
    list1.append("gst-lawyers")
    list1.append("immigration-lawyers")
    list1.append("labour-service-lawyers")
    list1.append("media-entertainment-lawyers")
    list1.append("medical-negligence-lawyers")
    list1.append("property-lawyers")
    list1.append("rti-lawyers")
    list1.append("armed-forces-tribunal-lawyers")
    list1.append("consumer-court-lawyers")
    cnt=0
    max_page=2
    for l1 in list1:
        base_url = f'https://lawrato.com/{l1}'
        cnt+=1
        page_number=1
        url = f'{base_url}?&page={page_number}'
        page_number+=1
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            lawyer_listings = soup.find_all('div', class_='lawyer-item border-box')
            for lawyer in lawyer_listings:
                name = lawyer.find('h2', class_='media-heading').text.strip()
                location = lawyer.find('div', class_='location').text.strip()
                experience = lawyer.find('div', class_='experience').text.strip()
                image_url = lawyer.find('img', class_='media-object')['src']
                area_skill_div = lawyer.find('div', class_='area-skill')
                practice_area_skills = "Criminal, Consumer Court"
                if area_skill_div:
                    div_contents = area_skill_div.find('div')
                    if div_contents:
                        practice_area_skills = div_contents.text.strip()
                rating = lawyer.find('span', class_='score').text.strip()
                advocate = Advocatefin(
                    name=name,
                    type=l1,
                    location=location,
                    experience=experience,
                    rating=rating,
                    image_url=image_url,
                    practice_area_skills=practice_area_skills  
                )
                print(name,type)
                # cat = Advocatecatagoryfin(cat=l1)
                # cat.save()
                # advocate.save()

            else:
                print(f"Failed to retrieve the page for {l1}. Status code:", response.status_code)

    return render(request,'navebar.html')

def webscrapdatapage2(request):
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
    list1.append("wills-trusts-lawyers")
    list1.append("copyright-patent-trademark-lawyers")
    list1.append("court-marriage-lawyers")
    list1.append("domestic-violence-lawyers")
    list1.append("gst-lawyers")
    list1.append("immigration-lawyers")
    list1.append("labour-service-lawyers")
    list1.append("media-entertainment-lawyers")
    list1.append("medical-negligence-lawyers")
    list1.append("property-lawyers")
    list1.append("rti-lawyers")
    list1.append("armed-forces-tribunal-lawyers")
    list1.append("consumer-court-lawyers")
    cnt=0
    max_page=2
    for l1 in list1:
        base_url = f'https://lawrato.com/{l1}'
        cnt+=1
        page_number=1
        url = f'{base_url}?&page={page_number}'
        page_number+=1
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            lawyer_listings = soup.find_all('div', class_='lawyer-item border-box')
            for lawyer in lawyer_listings:
                name = lawyer.find('h2', class_='media-heading').text.strip()
                location = lawyer.find('div', class_='location').text.strip()
                experience = lawyer.find('div', class_='experience').text.strip()
                image_url = lawyer.find('img', class_='media-object')['src']
                area_skill_div = lawyer.find('div', class_='area-skill')
                practice_area_skills = "Criminal, Consumer Court"
                if area_skill_div:
                    div_contents = area_skill_div.find('div')
                    if div_contents:
                        practice_area_skills = div_contents.text.strip()
                rating = lawyer.find('span', class_='score').text.strip()
                advocate = Advocatefin(
                    name=name,
                    type=l1,
                    location=location,
                    experience=experience,
                    rating=rating,
                    image_url=image_url,
                    practice_area_skills=practice_area_skills  
                )
                # cat = Advocatecatagoryfin(cat=l1)
                # cat.save()
                advocate.save()

            else:
                print(f"Failed to retrieve the page for {l1}. Status code:", response.status_code)

    return render(request,'navebar.html')











def arbitration_mediation_lawyers_data(request):
    # Define the URL you want to scrape
    url = 'https://www.leadindia.law/arbitration-and-mediation-lawyers'

    # Set a custom User-Agent header to mimic a real web browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    # Create a session to manage cookies
    session = requests.Session()
    response = session.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the lawyer listings within the specified class
        lawyer_listings = soup.find_all('div', class_='card shadow card-hover-shadow p-2')

        # Loop through all the lawyer listings
        for lawyer in lawyer_listings:
            # Extract lawyer's name
            name_element = lawyer.find('h6').find('a')
            name = name_element.text.strip() if name_element else None

            # Extract lawyer's rating
            rating_element = lawyer.find('li', class_='list-inline-item ms-0 h6 small fw-bold mb-0')
            rating = rating_element.text.strip() if rating_element else None

            # Extract lawyer's experience
            small_elements = lawyer.find_all('small')
            if len(small_elements) >= 3:
                experience = small_elements[0].get_text(strip=True)
                location = small_elements[1].get_text(strip=True)
                language = small_elements[2].get_text(strip=True)
            else:
                experience = location = language = None

            # Extract lawyer's practice areas
            practice_areas_element = lawyer.find('p', class_='p-0 m-0 h-75')
            practice_areas = practice_areas_element.text.strip() if practice_areas_element else None

            # Extract lawyer's contact link
            contact_link_element = lawyer.find('a', class_='btn btn-xs btn-dark')
            contact_link = contact_link_element['href'] if contact_link_element else None

            # Extract lawyer's photo URL
            photo_element = lawyer.find('img', class_='card-img')
            photo_url = photo_element['src'] if photo_element else None

            # # print or store the extracted information for each lawyer, including photo URL
            lawyer_instance =Aribitration_mediator(
            name=name,
            rating=rating,
            experience=experience,
            location=location,
            practice_areas=practice_areas,
            language=language,
            photo_url=photo_url,
            contact_link=contact_link
            )
            lawyer_instance.save()
    else:
        print(f"Failed to retrieve the page. Status code:", response.status_code)

    return render(request, 'navebar.html')


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
                names_to_exclude = ["Advocate Raman Jain","Advocate Hemant Kumar Joshi"]
                distinct_names = Advocatefin.objects.exclude(name__in=names_to_exclude).values('name').distinct().order_by('-rating')[:6]
                advocates_list = []

                for name_dict in distinct_names:
                    name = name_dict['name']
                    advocate = Advocatefin.objects.filter(name=name).first()  # Assuming there's only one advocate with a given name
                    if advocate:
                        advocates_list.append(advocate)
                # # print(type(advocates))
                # print(advocates_list)
                            # 'Lawyers': advocates
                context['Lawyers']=advocates_list
                
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
                distinct_names = Advocatefin.objects.values('name').distinct()[:6]
                advocates = Advocatefin.objects.filter(name__in=Subquery(distinct_names))
                # 'Lawyers': advocates
                names_to_exclude = ["Advocate Raman Jain","Advocate Hemant Kumar Joshi"]
                distinct_names = Advocatefin.objects.exclude(name__in=names_to_exclude).values('name').distinct().order_by('-rating')[:6]
                advocates_list = []

                for name_dict in distinct_names:
                    name = name_dict['name']
                    advocate = Advocatefin.objects.filter(name=name).first()  # Assuming there's only one advocate with a given name
                    if advocate:
                        advocates_list.append(advocate)
                # # print(type(advocates))
                # print(advocates_list)
                            # 'Lawyers': advocates
                context['Lawyers']=advocates_list
                        
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

@login_required
def upload_photo(request):
    if request.method == 'POST' and 'profile_photo' in request.FILES:
        user_profile = UserProfilePhoto.objects.get_or_create(user=request.user)[0]
        user_profile.photo = request.FILES['profile_photo']
        user_profile.save()
    return redirect('profile')    
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
                # print(lawyer)
                context = {
                    'obj': obj,
                    'user_d': user_d,
                    'user_status': user_status,
                    #  'lawyer':lawyer,
                    'lawyer':lawyer
                }
                names_to_exclude = ["Advocate Raman Jain","Advocate Hemant Kumar Joshi"]
                distinct_names = Advocatefin.objects.exclude(name__in=names_to_exclude).values('name').distinct().order_by('-rating')[:6]
                advocates_list = []

                for name_dict in distinct_names:
                    name = name_dict['name']
                    advocate = Advocatefin.objects.filter(name=name).first()  # Assuming there's only one advocate with a given name
                    if advocate:
                        advocates_list.append(advocate)
                # # print(type(advocates))
                # print(advocates_list)
                            # 'Lawyers': advocates
                context['Lawyers']=advocates_list
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
        names_to_exclude = ["Advocate Raman Jain","Advocate Hemant Kumar Joshi"]
        distinct_names = Advocatefin.objects.exclude(name__in=names_to_exclude).values('name').distinct().order_by('-rating')[:6]
        advocates_list = []

        for name_dict in distinct_names:
            name = name_dict['name']
            advocate = Advocatefin.objects.filter(name=name).first()  # Assuming there's only one advocate with a given name
            if advocate:
                advocates_list.append(advocate)
        # # print(type(advocates))
        # print(advocates_list)
                    # 'Lawyers': advocates
        context['Lawyers']=advocates_list
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
    # names_to_exclude = ["Advocate Raman Jain","Advocate Hemant Kumar Joshi"]
    # distinct_names = Advocatefin.objects.exclude(name__in=names_to_exclude).values('name').distinct().order_by('-rating')[:6]
    # # print(distinct_names)
    # advocates_list = []
    # # ad=Advocatefin.objects.all()
    # # # print(len(ad))

    # for name_dict in distinct_names:
    #     name = name_dict['name']
    #     advocate = Advocatefin.objects.filter(name=name).first()  # Assuming there's only one advocate with a given name
    #     if advocate:
    #         advocates_list.append(advocate)
    # # print(type(advocates))
    # # print(advocates_list)
                # 'Lawyers': advocates
    advocates_list=Advocatefin.objects.all()
    adv1=[]
    cnt=0
    for l1 in advocates_list:
        adv1.append(l1)
        cnt+=1
        if cnt==6:
            break
    context['Lawyers']=adv1
    # return render(request, 'index2.html',context)
    try:
        if request.user.is_authenticated:
            return render(request, 'index2.html')
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
    advocates_list=Advocatefin.objects.all()
    adv1=[]
    cnt=0
    for l1 in advocates_list:
        adv1.append(l1)
        cnt+=1
        if cnt==6:
            break
    context['Lawyers']=adv1
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
            sz=len(obj)
            advocates = Advocatefin.objects.all()[:sz]
            ziped_list=list(zip(obj,advocates))
            # # print(ziped_list)
            # # print(advocates)
            # print(obj)
            context = {'obj': obj,'advocates':advocates,'ziped_list':ziped_list}
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
        pass
    else : 
        chat_request = ChatRequest.objects.get(pk=receiver_id)
        pass
    return render(request,'navebar.html')



    
    
    


def readmore(request, id1, id2):
    try:

        if request.method == "GET":
            
            obj = Blog.objects.filter(pk=id1)
            lawyer=Advocatefin.objects.filter(pk=id2)
            context = {
                'obj': obj[0],
                'lawyer':lawyer[0]
            }
            blog = Blog.objects.all()[:4]
           
            sz=len(blog)
            # print(sz)
            # print(blog)
            advocates = Advocatefin.objects.all()[:sz]
            # print(advocates)
            ziped_list=list(zip(blog,advocates))
            # print(ziped_list)
            # print(len(ziped_list))
            context['ziped_list']=ziped_list
            return render(request, 'blogafteropen.html', context)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'error_page.html', {'error_message': error_message})

def dashboard(request):
    try:
        # # print(request.user.username)
        # user=User_detail.objects.filter(pk=request.user.id)
        # # print(user)
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
        # print(lawyer)
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
        # print(lawyer)
        chatrequest=ChatRequest.objects.filter(receiver=lawyer[0])
        cnt=len(chatrequest)
        # print(cnt)
        context={
            'lawyer':lawyer[0],
            'cnt':cnt
        }
        if cnt!=0:
            context['chatrequest']=chatrequest[0]
        # print(context)
        # return render(request,'navebar.html')
        return render(request, 'lawyer.html',context)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'error_page.html', {'error_message': error_message})




def accept_chat_request(request, request_id):
    try:
        chat_request = ChatRequest.objects.get(pk=request_id)
        chat_request.accepted = True
        chat_request.save()
        return redirect('chat', chat_request.receiver.id)
    except Exception as e:
        # print(str(e))  
        
        return render(request, 'error.html', {'error_message': 'An error occurred while processing your request'})


@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, id1,id2):
    room = Room.objects.get(pk=id2)
    lawyer=Laweruser.objects.filter(pk=id1)
    # print(lawyer)
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
    # write logic baad me not in priority
    try:
        # # print(request.user.username)
        # user=User_detail.objects.filter(pk=request.user.id)
        # # print(user)
        # return render(request,'navebar.html')
        # if request.method=="POST":
        #     User.username=request.user.username
        #     User.email=request.POST['email']
        #     User.first_name=request.POST['first_name']
        #     User.last_name=request.POST['last_name']
        #     User.save()
            
        return render(request, 'profile.html')
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'error_page.html', {'error_message': error_message})




def consult(request):
    try:
        return render(request, 'problem.html')
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'error.html', {'error_message': error_message})




def submitproblem(request):
    try:
        if request.method == "POST":
            city = request.POST.get('city', '')
            problem = request.POST.get('problem', '')
            # print(city)
            # print(problem)
            if not city or not problem:
                error_message = "Both 'city' and 'problem' are required."
                return render(request, 'problem.html', {'error_message': error_message})

            user_message = problem
            res = fn(request)
            user_message += " "
            user_message += res
            # print(user_message)

            gpt3_response = get_gpt3_response(user_message)
            gpt3_response = gpt3_response.lower()
            item = lawerexactmatch(request)
            lawyeritem = lawerecatagoryexactmatch(request)
            ans = ""
            ind = 0

            for i1 in item:
                if gpt3_response.find(i1) != -1:
                    ans = lawyeritem[ind]
                    break
                ind += 1

            # print(ans)

            if len(ans) == 0:
                ans += "criminal-lawyers"
            advocates = Advocatefin.objects.filter(type=ans)

            return render(request, 'lawyerCard.html', {'Lawyers': advocates})
    
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'error.html', {'error_message': error_message}, status=500)
    
    return render(request, 'problem.html')

    # return render(request, 'your_form_template.html')


def advocates_by_type(request, advocate_type):
    advocates = Advocatefin.objects.filter(type=advocate_type)
    return render(request, 'lawyerCard.html', {'Lawyers': advocates})
def advocates_by_id(request,id1):
    advocates = Advocatefin.objects.filter(pk=id1)
    for l in advocates:
        l.type=l.practice_area_skills
    return render(request, 'lawyerCard.html', {'Lawyers': advocates})


def searchlawyer(request):
    # print(-1)
    if request.method == "POST":
        search_query = request.POST.get("searchval")
        # print(search_query)
        advocates = Advocatefin.objects.filter(name__icontains=search_query)
        context={

        }
        if len(advocates) ==0:
            context['Lawyers']=advocates
            context['cn']=len(advocates)
        else:
            l11=[]
            l11.append(advocates[0])
            context['Lawyers']=l11
            context['cn']=len(advocates)

       
       
        return render(request, 'lawyerCard.html', context)
    else:
        lawyer=Laweruser.objects.all()

    # logout(request)
        context = {
            #  'lawyer':lawyer,
            'lawyer':lawyer

        }
        names_to_exclude = ["Advocate Raman Jain","Advocate Hemant Kumar Joshi"]
        distinct_names = Advocatefin.objects.exclude(name__in=names_to_exclude).values('name').distinct().order_by('-rating')[:6]
        advocates_list = []

        for name_dict in distinct_names:
            name = name_dict['name']
            advocate = Advocatefin.objects.filter(name=name).first()  # Assuming there's only one advocate with a given name
            if advocate:
                advocates_list.append(advocate)
        # # print(type(advocates))
        # # print(advocates_list)
                    # 'Lawyers': advocates
        context['Lawyers']=advocates_list
        context['cn']=5
        return render(request, 'index2.html',context)
 

def somebestadvocates(request):

    lawyer=Laweruser.objects.all()
    # logout(request)
    context = {
        #  'lawyer':lawyer,
        'lawyer':lawyer
    }
    names_to_exclude = ["Advocate Raman Jain","Advocate Hemant Kumar Joshi"]
    distinct_names = Advocatefin.objects.exclude(name__in=names_to_exclude).values('name').distinct().order_by('-rating')[:6]
    advocates_list = []

    for name_dict in distinct_names:
        name = name_dict['name']
        advocate = Advocatefin.objects.filter(name=name).first()  
        if advocate:
            advocates_list.append(advocate)

    # # print(type(advocates))
    # # print(advocates_list)
                # 'Lawyers': advocates
    context['Lawyers']=advocates_list
    return render(request, 'somebestadvocates.html',context)

def Arbitrators_Mediators(request):
    try:
        advocates = Aribitration_mediator.objects.all()
        return render(request, 'Arbitrators_Mediators.html', {'Lawyers': advocates})
    except Aribitration_mediator.DoesNotExist:
        return render(request, 'error.html', {'error_message': 'No lawyers found.'})
    except Exception as e:
        return render(request, 'error.html', {'error_message': f"An error occurred: {e}"})




  



    
    






