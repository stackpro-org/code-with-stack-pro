import pathlib
import random
import uuid

from django.utils.text import slugify



def random_string_generator():
    
    size = 4
    chars = ['a','v','r','y','8','6','2','9']
   
    #  to know about join https://www.w3schools.com/python/ref_string_join.asp

    random_code = "".join(random.choice(chars) for _ in range(size))
    return random_code


def unique_slug_generator(instance, new_slug=None):
    #by instance we get the following model
   

    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.headline)


    # we access to 'blog.models.Post' by the bellow code
    Klass = instance.__class__
    
    # this query will search in database is there any slug like the existed one
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        # to understand format https://www.w3schools.com/python/trypython.asp?filename=demo_ref_string_format2
        new_slug = "{slug}-{randstr}".format(
            slug=slug, randstr=random_string_generator()
        )

        # here 'unique_slug_generator' is called again
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug