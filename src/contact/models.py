
from django.db import models

class Top_contact(models.Model):


    title = models.CharField(max_length=25)
    address = models.CharField(max_length=50)
    def __str__(self):
        return self.title


class Top_contact2(models.Model):


    title = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    def __str__(self):
        return self.title


class Top_contact3(models.Model):


    title = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=50)
    def __str__(self):
        return self.title


class Contact(models.Model):

    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=40)
    message = models.TextField(max_length=400)

    def __str__(self):
        return self.name


