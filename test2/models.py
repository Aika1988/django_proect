from django.db import models
from test1.models import Post

class Comment(models.Model):
    comment = models.TextField()
    post_comment= models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='posts'
    )


    def __str__(self):
        return self.comment 
    
