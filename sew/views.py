from re import A
from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from urllib import request
from sew.models import Reach, Customer_Signup,Tailor_Signup
from django.contrib import messages
# Create your views here.


def home(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        mail = request.POST.get('mail')
        phone = request.POST.get('phone')
        # Password=request.POST.get('Password')

        desc = request.POST.get('desc')
        reach = Reach(firstname=firstname, lastname=lastname,
                      mail=mail, phone=phone, desc=desc)
        reach.save()
        messages.success(request, 'Your message has been sent.')
    # return HttpResponse('main page')
    return render(request, 'home.html')


def about(request):
    # return HttpResponse('about us')
    return render(request, 'about.html')


def signin(request):
    # return HttpResponse('contact us')
    return render(request, 'signin.html')


def login(request):
    # return HttpResponse('to looged in'
    # )
    if request.method == 'POST':
        # if 'customername' in request.POST:
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        mail = request.POST.get('mail')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        address = request.POST.get('address')
        customer_signup = Customer_Signup(firstname=firstname, lastname=lastname, mail=mail, phone=phone, password=password, address=address)
        customer_signup.save()
        # elif 'tailorname' in request.POST:
        #     
    return render(request, 'login.html')
def tailor(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        mail = request.POST.get('mail')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        shopname = request.POST.get('shopname')
        address = request.POST.get('address')
        tailor_signup = Tailor_Signup(firstname=firstname, lastname=lastname, mail=mail, phone=phone, password=password,shopname=shopname, address=address)
        tailor_signup.save()
    return render(request, 'tailor.html')
