# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import contactForm
from django.conf import settings


def contact(request):
    title = 'Contact Us Today'
    form = contactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        print request.POST
        name = form.cleaned_data['name']
        message = form.cleaned_data['message']
        subject = 'Message from Mysite.com'
        message = '%s %s' %(message,name)
      #  emailFrom = form.cleaned_data['phonenumber']
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject,message,emailFrom,emailTo,fail_silently=True )
        title = "Thanks!"
        confirm_message = "Thanks For the Message.We Will get right back to you As Soon As Possible"
        form = None
        
    context = {'title':title,'form':form,'confirm_message':confirm_message }
    template = 'contact.html'
    return render(request,template,context)

