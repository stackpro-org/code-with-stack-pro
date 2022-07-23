import random
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Category(models.Model):

    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
      self.name = self.name.lower()
      return super(Category, self).save(*args, **kwargs)


def random_code():
    ran =['2','6','q','v','x','9']
    size = 4
    randomsl = "".join(random.choice(ran) for x in range(size))
    return randomsl


def unique_slug_generator(instance):
  
    new_slug = slugify(instance.title)
    
    klass = instance.__class__

    check = klass.objects.filter(slug = new_slug).exists()
    if check:
        slug = "{slug}-{code}".format(slug= new_slug, code=random_code())
    else:
        slug = new_slug

    return slug






class Portfolio(models.Model):

    catagory = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    client_name = models.CharField(max_length=50)
    project_date = models.DateTimeField(default=timezone.now)
    Project_url = models.URLField(max_length=100, null=True, blank=True)
    image1 = models.ImageField(upload_to='',)
    image2 = models.ImageField(upload_to='', null=True, blank=True)
    image3 = models.ImageField(upload_to='', null=True, blank=True)
    image4 = models.ImageField(upload_to='', null=True, blank=True)

    description = models.TextField(max_length=400)

    def __str__(self):
        return self.client_name

    
    
    def save(self, *args, **kwargs):
        self.slug = unique_slug_generator(self)
        super().save(*args, **kwargs)
    




