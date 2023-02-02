from django.db import models
from test2.models import Comment

class Post(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='images/')
    post = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    def __str__(self):
        return self.name




