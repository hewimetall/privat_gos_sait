from django.db import models

# Create your models here.
class Contact_bd(models.Model):
    name  = models.CharField(max_length=20,null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=11,null=True)
    text  = models.TextField(max_length=200,blank=True)
    date  = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name="Таблица со списком обратной формы"
        verbose_name_plural="Таблица со списком запросов из  обратной формы"