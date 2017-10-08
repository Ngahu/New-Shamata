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
    template = 'index.html'
    return render(request,template,context)



def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # message success
        #messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
        "title": "Create Property Listing",
    }
    template = 'property-create.html'
    return render(request, template, context)


def post_update(request,slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    template = 'property-create.html'
    return render(request, template, context)


def post_detail(request,slug=None):#   showing details
    instance = get_object_or_404(Post, slug=slug)
    context = {
        "instance": instance,
    }
    template = 'detail.html'
    return render(request,template, context)

#this is the listing of all propertis in the database
def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list":queryset,
        "title":"listng"
    }
    template = 'singleproperty.html'
    return render(request,template,context) 



#List only 8 properties from the database
def property_listing(request):
    queryset_list = Post.objects.all()
    queryset_members = Team_Meamber.objects.all()
    paginator = Paginator(queryset_list,8)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    
    context = {
        "object_list":queryset,
        "title":"List of Properties",
        "members_list": queryset_members,
    }
    template = 'index.html'
    return render(request,template,context)

    


def post_delete(request,slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post,slug=slug)
    instance.delete()
    return redirect("Main:home")


def dash_board(request):# incharge of the secong dmin panell for editing the website
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    context = {
         "title":"Welcome to the  Dashboard",
         "title_small":" Admin Overview"
    }
    return render(request,"dashboard.html",context)

def dash_board_help(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    context = {
        "title":"Help Page",
    }
    template = 'dashboard_help.html'

    return render(request,template,context)




def add_member(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = TeamForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # message success
        #messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url_2())

    context = {
        "title":"Add Company Member",
        "form": form,
    }
    return render(request,"Add_member.html",context)



def single_members_details(request,id=None): #Detail
    instance_2 = get_object_or_404(Team_Meamber, id=id)
    context = {
        "instance_2": instance_2,
    }
    return render(request,"member's_detail.html",context)

