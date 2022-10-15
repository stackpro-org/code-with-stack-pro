from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from account.models import Account
from django.utils import timezone
from django.urls import reverse
from django.db.models import Q
from . import utils

from io import BytesIO
from PIL import Image
from django.core.files import File
print('hello hhh')
def compress(image):
    im = Image.open(image)
    im_io = BytesIO() 
    im.save(im_io, 'JPEG', quality=10) 
    new_image = File(im_io, name=image.name)

    return new_image


class Category(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
      return self.name



class AgentQuerySet(models.QuerySet):
    def is_publuish(self):
        return self.filter(publish_status=Post.ArticlePublishOptions.PUBLISH)

    # we find the finding method's arguments from views.py
    def finding(self, query):
        lookup = Q(headline__icontains=query) | Q(body__icontains=query)
        qs = self.is_publuish().filter(lookup)
        return qs

class AgentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        # to know detail https://docs.djangoproject.com/en/4.0/topics/db/managers/
        return AgentQuerySet(self.model, using=self._db)



class Post(models.Model):
      class ArticlePublishOptions(models.TextChoices):
         PUBLISH = "pub", "Publish"
         DRAFT = "dra", "DRAFT"
         PRIVATE = "pri", "Private"

      catagory = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
      headline = models.CharField(max_length=240,help_text="Headline of the article",)
      sub_headline = models.CharField(max_length=250 , blank=True, null=True)
      thumbnail = models.ImageField(blank=True,null=True,upload_to='images/')
      body = RichTextField()
      author = models.ForeignKey(Account, blank=True,on_delete= models.CASCADE, related_name='blog_post')
      slug = models.SlugField(blank=True,null=True)
      publish_status = models.CharField(
        max_length=3,
        choices=ArticlePublishOptions.choices,
        default=ArticlePublishOptions.DRAFT,)
      published = models.DateTimeField(default=timezone.now)
      created = models.DateTimeField(auto_now_add=True)
      objects = AgentManager()

      def get_absolute_url(self):
          return reverse("blog:post_detail", args=[self.slug])

      def get_image_url(self):
         if not self.thumbnail:
            return None
         return self.thumbnail.url


      class Meta:
            ordering = ('-published',)
      

      def __str__(self):
            return self.headline
      

      def save(self, *args, **kwargs):
        
          
        if not self.slug:

            self.slug = utils.unique_slug_generator(self)
        if self.thumbnail:
           new_image = compress(self.thumbnail)
           self.thumbnail = new_image
        super().save(*args, **kwargs)


class Comments(models.Model):
      post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_here')
      name = models.CharField(max_length=30)
      email = models.EmailField()
      comment = models.TextField(max_length=200)
      approved = models.BooleanField(default=False,null=True)
      date = models.DateTimeField(auto_now_add=True)

      def __str__(self):
          return self.comment



