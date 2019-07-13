from django.db import models

# Create your models here.
class Contact_bd(models.Model):
    name  = models.CharField(max_length=20,null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=11,null=True)
    text  = models.TextField(max_length=200,blank=True)
    date  = models.DateTimeField(auto_now=True)
    class __Meta__:
        order_by=['date']