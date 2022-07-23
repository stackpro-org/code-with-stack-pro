from django.db import models



class Service(models.Model):

    title = models.CharField(max_length=264)
    url = models.URLField(max_length=264)
    text = models.TextField(max_length=500)
    def __str__(self):
        return self.title


class Skill(models.Model):
  
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=400)
    img = models.ImageField(upload_to='')
    title2 = models.CharField(max_length=100)
    html = models.TextField(max_length=4)
    css = models.TextField(max_length=4)
    javascript = models.TextField(max_length=4)
    photoshop = models.TextField(max_length=4)
    def __str__(self):
        return self.title