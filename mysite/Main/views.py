# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404 ,HttpResponseRedirect
# Create your views here.
from .forms import PostForm
from .forms import TeamForm
from django.shortcuts import render, get_object_or_404, redirect
from  .models import Post
from  .models import Team_Meamber
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q






def home(request):
    context ={
        "title":"this is the home page"
    }
    template = 'property-listing.html'
    return render(request,template,context)