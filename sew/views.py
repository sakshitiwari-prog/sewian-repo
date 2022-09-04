from re import A
from django.http import HttpResponse
from django.shortcuts import redirect, render,HttpResponse
from urllib import request
from sew.models import Reach
from django.contrib import messages
# Create your views here.
def home(request): 
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        mail=request.POST.get('mail')
        phone=request.POST.get('phone')
        # Password=request.POST.get('Password')

        desc=request.POST.get('desc')
        reach=Reach(firstname=firstname,lastname=lastname,mail=mail,phone=phone,desc=desc)
        reach.save()
        messages.success(request, 'Your message has been sent.')
    # return HttpResponse('main page')
    return render(request,'home.html') 
def about(request):
    # return HttpResponse('about us')
    return render(request,'about.html')
def account(request):
    # return HttpResponse('contact us')
    return render(request,'account.html')
def login(request):
    # return HttpResponse('to looged in'
    #)
    # if request.method=='POST':
    #     first_name=request.POST.get('first_name')
    #     last_name=request.POST.get('last_name')
    #     mail=request.POST.get('mail')
    #     phone=request.POST.get('phone')
    #     Password=request.POST.get('Password')
    #     Address=request.POST.get('Address')
    #     login=Login(first_name=first_name,last_name=last_name,mail=mail,phone=phone,Password=Address)
    #     Login.save()
    return render(request,'login.html')
