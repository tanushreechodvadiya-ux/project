from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render , redirect
from .models import *


def index (request):
    return render(request,"index.html")

def fetchcontact(request):
     if request.method == 'POST':
            name = request.POST.get("cname")
            email = request.POST.get('email')
            message = request.POST.get('message')
            file = request.FILES.get('file')
            submitted_at = request.POST.get('submitted_at')

            insertquery =ContactMessage(cname=name, email=email, message=message, file=file, submitted_at=submitted_at)
            insertquery.save()

            messages.success(request, "Sent successfully")
            return redirect("/")

def lifeinsurance(request):
    return render(request,"lifeinsurance.html")

def longtermcareplanningpage(request):
    return render(request,"longtermcareplanning.html")

def retirementpage(request):
    return render(request,"retirement.html")

def estateplanningpage(request):
    return render(request,"estateplanning.html")

def wealthmanagementpage(request):
    return render(request,"wealthmanagement.html")

def collegeplanningpage(request):
    return render(request,"collegeplanning.html")