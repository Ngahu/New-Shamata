# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404,HttpResponseRedirect
from django.shortcuts import render
from .models import Property,TeamMember
# Create your views here.


def home(request):
    context ={
        "title":"title"
    }
    template = 'index.html'
    return render(request,template,context)

#this is incharge of creating the property 
def property_create(request):
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