from django.db import models
from account.models import Account
# Create your models here.


class PersonalChat(models.Model):
    user1 = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="usr1")
    user2 = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="usr2")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user1}, {self.user2}"
