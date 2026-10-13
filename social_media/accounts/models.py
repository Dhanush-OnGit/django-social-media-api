from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    email = models.CharField(max_length=20,unique=True)
    profile_image = models.ImageField(upload_to="profile/",null=True,blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username