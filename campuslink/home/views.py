from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import mysql.connector as sql 
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def index(request):

    email = request.POST.get('email')
    if(email==""):
        return render(request, 'index.html')
    
    if request.method == 'POST':

        send_mail('Welcome to CampusLink Event Notifications!','Thank you for subscribing to event notifications on CampusLink. \n\nFrom now on, you will receive timely updates and reminders about the latest events happening on our campus, including competitions, seminars, and workshops. We’re excited to keep you informed so you never miss out on opportunities to participate and engage.',
                'irfan.md2302@gmail.com', [email], fail_silently=False, )
    
    return render(request, 'index.html')

def login(request):
    email = request.POST.get('email', 'default')
    password = request.POST.get('password', 'default')

    if(email=="" or password==""):
        return render(request, 'error.html')
    
    if request.method=="POST":
        m = sql.connect(host="localhost", user="root", password="montforT&2020", database="campuslink")
        cursor = m.cursor()
        query = "SELECT * from users WHERE email=%s and password=%s"
        cursor.execute(query, (email, password))
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,"UserDashboard.html")

    return render(request, 'login.html')    

def register(request):

    email = request.POST.get('email', 'default')
    password = request.POST.get('password', 'default')
    rpassword = request.POST.get('password_repeat', 'default')
    
    if(email=="" or password!=rpassword):
        return render(request, 'register.html')

        
    if request.method=="POST":
        m = sql.connect(host="localhost", user="root", password="montforT&2020", database="campuslink")
        cursor = m.cursor()
        query = "INSERT INTO users (email, password) VALUES (%s, %s)"
        cursor.execute(query, (email, password))
        m.commit()
        return render(request, 'login.html')

    return render(request, 'register.html')

def events(request):

    email = request.POST.get('email')
    if(email==""):
        return render(request, 'eventlisting.html')
    
    if request.method == 'POST':

        send_mail('Welcome to CampusLink Event Notifications!','Thank you for subscribing to event notifications on CampusLink. \n\nFrom now on, you will receive timely updates and reminders about the latest events happening on our campus, including competitions, seminars, and workshops. We’re excited to keep you informed so you never miss out on opportunities to participate and engage.',
                'irfan.md2302@gmail.com', [email], fail_silently=False, )
            

    return render(request, 'eventlisting.html')

def regist(request):

    email = request.POST.get('email')
    if(email==""):
        return render(request, 'regist.html')
    
    if request.method == 'POST':

        send_mail('Welcome to CampusLink Event Notifications!','Thank you for subscribing to event notifications on CampusLink. \n\nFrom now on, you will receive timely updates and reminders about the latest events happening on our campus, including competitions, seminars, and workshops. We’re excited to keep you informed so you never miss out on opportunities to participate and engage.',
                'irfan.md2302@gmail.com', [email], fail_silently=False, )
        
    return render(request, 'regist.html')

def UserDashboard(request):
    email = request.POST.get('email')
    if(email==""):
        return render(request, 'UserDashboard.html')
    
    if request.method == 'POST':

        send_mail('Welcome to CampusLink Event Notifications!','Thank you for subscribing to event notifications on CampusLink. \n\nFrom now on, you will receive timely updates and reminders about the latest events happening on our campus, including competitions, seminars, and workshops. We’re excited to keep you informed so you never miss out on opportunities to participate and engage.',
                'irfan.md2302@gmail.com', [email], fail_silently=False, )
    return render(request, 'UserDashboard.html')