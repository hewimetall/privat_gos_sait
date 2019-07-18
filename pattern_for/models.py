from django.db import models
from markdownx import models as mk_models

class categoy(models.Model):
    name=models.CharField(max_length=200,primary_key=True)
    slug=models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering=['name']
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

# Create your models here.
class pattern_for(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField()
    text =mk_models.MarkdownxField(max_length=1200)
    categoy=models.ForeignKey(categoy,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='prod/',blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    date=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Запис в категориях"
        verbose_name_plural="Записи в категориях"

    def get_image(self):
        return  str( 'for_gos/'+self.image+".png")

    def __str__(self):
        return "{} {} ".format(self.name,self.categoy)
