from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class about_company(models.Model):
    def creat(selfs):
        pass

    def __str__(self):
        return '{}'.format(self.title)

class item_block(models.Model):
    item1=  models.CharField(max_length=40)
    item2 = models.CharField(max_length=40)
    item3 = models.CharField(max_length=40)
    item4 = models.CharField(max_length=40)

class list_menu(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(max_length=40,upload_to='about_company/')
    url = models.SlugField()

    def get_image(self):
        return  str( 'about_company/'+self.image+".png")
class car_news(models.Model):
    # file will be uploaded to MEDIA_ROOT/uploads
    upload = models.FileField(upload_to='about_company/')
