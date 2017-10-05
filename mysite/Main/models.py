# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from phonenumber_field.modelfields import PhoneNumberField
from django.core.urlresolvers import reverse
# Create your models here.



def upload_location(instance,filename):
    return "%s/%s" %(instance.id,filename)


class Property(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=upload_location)
    video = models.FileField(blank=True, null=True,upload_to='upload_location')
    description = models.TextField()
    size_of_land =models.CharField(max_length=500)
    location_details = models.CharField(max_length=1000)
    price = models.BigIntegerField(default=00.00)
    features = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Main:detail",kwargs={"slug":self.slug})
        

    class Meta:
        ordering = ["-timestamp", "-updated"]


    
# CREATING OF THE SLUG FOR THE PROPERTY 
#check if the slug exists and if it exists create a new one + id
def create_slug(instance,new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
        qs = Property.objects.filter(slug=slug).order_by("-id")
        exists = qs.exists()
        if exists:
            new_slug = "%s-%s" %(slug, qs.first().id)
            return create_slug(instance,new_slug=new_slug)
        return slug


def pre_save_property_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

#connecting with the signals
pre_save.connect(pre_save_property_receiver,sender=Property)




class TeamMember(models.Model):
    members_name = models.CharField(max_length=100)
    members_role = models.CharField(max_length=100)
    slug_name = models.SlugField(unique=True)
    members_details = models.TextField()
    members_phone_number = PhoneNumberField() #models.IntegerField(null=True,blank=True)
    members_email = models.EmailField()
    members_image = models.ImageField(upload_to=upload_location,blank=True, null=True)
    def __str__(self):
        return self.members_name


    def __unicode__(self):
        return self.members_name


def create_slug_member(instance,member_slug=None):
    slug_name = slugify(instance.members_name)
    if member_slug is not None:
        slug_name = member_slug
    qs = TeamMember.objects.filter(slug_name=slug_name).order_by("-id")
    exists = qs.exists()
    if exists:
        member_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug_member(instance,member_slug=member_slug)
    return slug_name

def pre_save_team_member_receiver(sender, instance, *args, **kwargs):
    if not instance.slug_name:
        instance.slug_name = create_slug_member(instance)



pre_save.connect(pre_save_team_member_receiver,sender=TeamMember)