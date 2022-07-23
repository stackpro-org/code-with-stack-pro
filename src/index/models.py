from django.db import models

class Hero(models.Model):
  
    title = models.CharField(max_length=264)
    lasttitle = models.CharField(max_length=264)
    description = models.TextField(max_length=1000)
    button = models.URLField(max_length=264)
    slideImg = models.ImageField(upload_to='slider/')
    def __str__(self):
        return self.title

class Featured(models.Model):


    title = models.CharField(max_length=264)
    url = models.URLField(max_length=264)
    text = models.TextField(max_length=1000)
    def __str__(self):
        return self.title

    
class Hi(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name











