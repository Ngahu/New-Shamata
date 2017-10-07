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


#example
queryset_members = Team_Meamber.objects.all()

#The home  Page View and passing all the templates and shit

def home(request):
    context = {
        "title": "HOME PAGE HOME",
        
    }
    return render(request, "base.html",context )


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
    return render(request, "Property_create.html", context)

def post_list(request):
    queryset_list = Post.objects.all()
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(location_details__icontains=query) |
            Q(description__icontains=query) |
            Q(description__icontains=query) |
            Q(features__icontains=query)
        ).distinct()

    paginator = Paginator(queryset_list, 6)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "title": "List",
        "no_item":"No items for you",
        "page_request_var": page_request_var,
        "members_list": queryset_members,
    }
    return render(request, "index.html", context)


def post_detail(request,slug=None):#   showing details
    instance = get_object_or_404(Post, slug=slug)
    context = {
        "instance": instance,
    }
    return render(request,"singleproperty.html", context)


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
    return render(request, "Post_create.html", context)



def post_delete(request,slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post,slug=slug)
    instance.delete()
    return redirect("Main:home")


#the all property list
def property_listing(request):
    queryset_list = Post.objects.all()
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(location_details__icontains=query) |
            Q(description__icontains=query) |
            Q(description__icontains=query) |
            Q(features__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, 6)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list": queryset,
        "title": "List",
        "no_item":"No items for you",
        "page_request_var": page_request_var,
        "members_list": queryset_members,
    }
    template = 'property_listing.html'
    return render(request,context)


#the  gallery view
def gallery(request):
    context = {}

    return render(request,"gallery.html",context)
    


def our_team(request):  #list
    queryset_members = Team_Meamber.objects.all()

    context = {
        "title": "Team  Page",
        "members_list": queryset_members,


    }
    return render(request,"our_team.html",context)



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




def dash_board(request):# incharge of the secong dmin panell for editing the website
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    context = {
         "title":"Welcome to the  Dashboard",
         "title_small":" Admin Overview"
    }
    return render(request,"dashboard.html",{})

def dash_board_help(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    context = {
        "title":"Help Page",
    }
    template = 'dashboard_help.html'

    return render(request,template,context)

