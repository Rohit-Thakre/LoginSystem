from django.db import models
from django.contrib.auth.models import AbstractUser, User
# Create your models here.

class cUser(User):
    profile_pic = models.ImageField(upload_to ='profile_pic/' ,blank=True, null=True)

    def __str__(self):
        return self.username
