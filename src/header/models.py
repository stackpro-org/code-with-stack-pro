from django.db import models

class Top_header(models.Model):

    fav_icon = models.ImageField(upload_to='')
    fav_icon2 = models.ImageField(upload_to='')
    number = models.CharField(max_length=20)
    email = models.EmailField()
    twitter = models.URLField()
    facebook = models.URLField()
    instagram = models.URLField()
    linkedin = models.URLField()
    def __str__(self):
        return self.email


class Header(models.Model):
    
    logo = models.CharField(max_length=25)
    def __str__(self):
        return self.logo
