from django.db import models
from markdownx.models import MarkdownxField

class Post(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    image_title = models.ImageField(upload_to='news/post/image/title')
    introduese=models.TextField(max_length=300)

    content=MarkdownxField(max_length=1200)
    date=models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering=['-date']
        verbose_name = "Список постов"
        verbose_name_plural="писок постов"


    def __str__(self):
        return self.title

