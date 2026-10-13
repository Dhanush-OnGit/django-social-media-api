from django.db import models
from accounts.models import CustomUser
from posts.models import Post
# Create your models here.

class Like(models.Model):
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="like")
    post_obj = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="like")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints=[
            models.UniqueConstraint(fields=["owner","post_obj"],name="unique_user_post_like")
        ]
    def __str__(self):
        return f"{self.owner.username} - {self.post_obj.title}"
