from django.db import models


class Top_footer1(models.Model):
    
    title = models.CharField(max_length=50)
    urlname1 = models.CharField(max_length=50)
    urlname2 = models.CharField(max_length=50)
    urlname3 = models.CharField(max_length=50)
    urlname4 = models.CharField(max_length=50)
    urlname5 = models.CharField(max_length=50)
    url1 = models.URLField(max_length=50)
    url2 = models.URLField(max_length=50)
    url3 = models.URLField(max_length=50)
    url4 = models.URLField(max_length=50)
    url5 = models.URLField(max_length=50)

    def __str__(self):
        return self.title


class Top_footer2(models.Model):

    title = models.CharField(max_length=50)
    urlname1 = models.CharField(max_length=50)
    urlname2 = models.CharField(max_length=50)
    urlname3 = models.CharField(max_length=50)
    urlname4 = models.CharField(max_length=50)
    urlname5 = models.CharField(max_length=50)
    url1 = models.URLField(max_length=50)
    url2 = models.URLField(max_length=50)
    url3 = models.URLField(max_length=50)
    url4 = models.URLField(max_length=50)
    url5 = models.URLField(max_length=50)

    def __str__(self):
        return self.title


class Top_footer3(models.Model):

    title = models.CharField(max_length=20)
    address1 = models.CharField(max_length=30)
    address2 = models.CharField(max_length=30)
    address3 = models.CharField(max_length=30)
    number = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.title


class Top_footer4(models.Model):
  
    title = models.CharField(max_length=20)
    short_text = models.CharField(max_length=200)
    twitter = models.URLField()
    facebook = models.URLField()
    instagram = models.URLField()
    linkedin = models.URLField()
    skype = models.URLField()
    copy_right = models.CharField(max_length=30)

    def __str__(self):
        return self.title
