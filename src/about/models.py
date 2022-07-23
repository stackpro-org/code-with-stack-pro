from django.db import models

class Count(models.Model):

    number = models.CharField(max_length=10)
    subtitle = models.CharField(max_length=100)
    shorttext = models.CharField(max_length=100)
    url = models.URLField(max_length=150)
    def __str__(self):
        return self.number

        
class Testimonial1(models.Model):

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=264)
    def __str__(self):
        return self.title


class Testimonial2(models.Model):


    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='testimonials')
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=264)
    def __str__(self):
        return self.name



class Client_image(models.Model):
    name = models.CharField(max_length=264, null=True, blank=True)
    image = models.ImageField(upload_to='clients', null=True, blank=True)

    def __str__(self):
        return str(self.name)

class Client(models.Model):

    title = models.CharField(max_length=264)
    text = models.TextField(max_length=500)
    client_image = models.ManyToManyField(Client_image, blank=True,)
    def __str__(self):
        return self.title



class About(models.Model):

  
    img = models.ImageField(upload_to='')
    title = models.CharField(max_length=264)
    text1 = models.TextField(max_length=1000)
    text2 = models.TextField(max_length=1000)
    def __str__(self):
        return self.title




