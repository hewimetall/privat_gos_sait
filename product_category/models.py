from django.db import models
from markdownx import models as mk_models

# Create your models here.

class name_cat(models.Model):
    name = models.CharField(max_length=30,primary_key=True)
    slug = models.SlugField()
    image = models.ImageField(upload_to='prod/catalog/name', blank=True)


class items_cat(models.Model):
    name = models.CharField(max_length=30,primary_key=True)
    slug = models.SlugField()
    text =mk_models.MarkdownxField(max_length=1200)
    image=models.ImageField(upload_to='prod/catalog/',blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    categoy=models.ForeignKey(name_cat,on_delete=models.CASCADE)


    def get_image(self):
        return  str( 'for_gos/'+self.image+".png")

    def __str__(self):
        return "{} {} ".format(self.name,self.categoy)

    def get_absolute_url(self):
        return "/mag/" + str(self.categoy)+ "/" + str(self.slug)+"/"
