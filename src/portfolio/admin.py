from django.contrib import admin
from .models import *

admin.site.register(Category)



@admin.register(Portfolio)
class PostCodesAdmin(admin.ModelAdmin):
  exclude = ('slug',)