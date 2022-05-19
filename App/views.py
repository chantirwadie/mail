import re
from django.http import HttpResponse
from rest_framework.response import Response
from django.shortcuts import render
from .Helper import sendMail
# Create your views here.


def index(request):
    return render(request, 'index.html')

def send_mail(request):

    if request.method == "POST":
        email = "ibrahimchahboune@gmail.com"
        subject = "Testing the subject"
        mydict = {'last_name': 'Chahboune', 'email': email, 'password': '123456789'}
        html_template = 'test2.html'
        sendMail([email, "ibrahimofficiel20@gmail.com"], subject, html_template, mydict)
        return HttpResponse("Email sent") 

def resetPassword(request):

    if request.method == "POST":
        email = request.POST.get('email')
        created_at = request.POST.get('created_at')
        expired_at = request.POST.get('expired_at')
        last_name = request.POST.get('last_name')
        link = request.POST.get('link')

        subject = "Réinitialisation"
        mydict = {'last_name': last_name, 'created_at': created_at, 'link': link, 'expired_at': expired_at}
        html_template = 'reset_password_template.html'
        sendMail([email], subject, html_template, mydict)
        
        return HttpResponse("Email sent")
