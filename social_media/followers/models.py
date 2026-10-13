from django.db import models
from accounts.models import CustomUser
# Create your models here.

class Followers(models.Model):
    following = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="following")
    follower = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="follower")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.following.username} follows {self.follower.username}"
