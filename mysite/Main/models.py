# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings
# Create your models here.
from django.db.models.signals import pre_save
from django.utils.text import slugify
# phone number
from phonenumber_field.modelfields import PhoneNumberField


#########

def upload_location(instance,filename):
    return "%s/%s" %(instance.id,filename)


class Team_Meamber(models.Model):
    members_name = models.CharField(max_length=100)
    members_role = models.CharField(max_length=100)
    slug_name = models.SlugField(unique=True)
    members_details = models.TextField()
    members_phone_number = PhoneNumberField(blank=True, null=True)
    members_email = models.EmailField()
    members_image = models.ImageField(upload_to=upload_location,) #null=False,blank=False
    

    def __str__(self):
        return self.members_name


    def __unicode__(self):
        return self.members_name


    def get_absolute_url_2(self):
        return reverse("Main:single_member_detail",kwargs={"id": self.id})
    


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=upload_location)
    image_2 = models.ImageField(upload_to=upload_location)
    image_3 = models.ImageField(upload_to=upload_location,blank=True, null=True)
    image_4 = models.ImageField(upload_to=upload_location,blank=True, null=True)
    image_5 = models.ImageField(upload_to=upload_location,blank=True, null=True)
            #width_field="width_field",
            #height_field="height_field")
    #height_field = models.IntegerField(default=0)
    #width_field = models.IntegerField(default=0)
    video = models.FileField(upload_to=upload_location,blank=True, null=True)
    description = models.TextField()
    size_of_land = models.IntegerField()
    location_details = models.CharField(max_length=300)
    price = models.IntegerField()
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


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)



pre_save.connect(pre_save_post_receiver, sender=Post)



def create_slug_member(instance,member_slug=None):
    slug_name = slugify(instance.members_name)
    if member_slug is not None:
        slug_name = member_slug
    qs = Team_Meamber.objects.filter(slug_name=slug_name).order_by("-id")
    exists = qs.exists()
    if exists:
        member_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug_member(instance,member_slug=member_slug)
    return slug_name

def pre_save_team_member_receiver(sender, instance, *args, **kwargs):
    if not instance.slug_name:
        instance.slug_name = create_slug_member(instance)



pre_save.connect(pre_save_team_member_receiver,sender=Team_Meamber)