from django.db import models
from accounts.models import CustomUser
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to="post/")
    description = models.TextField()
    craeted_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="post")

    def __str__(self):
        return self.title
