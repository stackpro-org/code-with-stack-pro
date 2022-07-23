from django.db import models


class Team(models.Model):

    img = models.ImageField(upload_to='team/')
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    text = models.TextField(max_length=264)
    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
