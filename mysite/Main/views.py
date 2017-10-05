# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Property,TeamMember
# Create your views here.


def home(request):
    context ={
        "title":"title"
    }
    template = 'index.html'
    return render(request,template,context)