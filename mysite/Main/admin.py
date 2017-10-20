# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post, Team_Meamber,Sell_to_us
# Register your models here.

admin.site.register(Post)
admin.site.register(Team_Meamber)
admin.site.register(Sell_to_us)