from django.contrib import admin
from .models import *

admin.site.register(Category)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('headline','author','publish_status','published')  
    prepopulated_fields = {'slug':('headline',)}
    
@admin.register(Comments)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name','comment','email')


