# from django.db.models.signals import post_save, pre_save
# from account.models import Account
# from .models import Profile
# from django.dispatch import receiver
# import random

# def random_code():
#     code = ['1','2','3','0','4','5','6','7']
#     ran = "".join(random.choice(code) for x in range(6))
#     return ran

# @receiver(post_save, sender=Account)
# def create_profile(sender, instance, created,  **kwargs):

#     if created:

#         Profile.objects.create(
#             user=instance,
#             email=instance.email,
#             auth_token=random_code()

#         )
