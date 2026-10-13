from django.db import models
from accounts.models import CustomUser
from posts.models import Post
# Create your models here.

class Comments(models.Model):
    comment = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='comments')
    post_obj = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')

    def __str__(self):
        return self.comment
