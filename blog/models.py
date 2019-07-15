from django.db import models
from markdownx.models import MarkdownxField

class Post(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    image_title = models.ImageField(upload_to='news/image/title')
    introduese=models.TextField(max_length=300)

    content=MarkdownxField(max_length=1200)

    def __str__(self):
        return self.title

