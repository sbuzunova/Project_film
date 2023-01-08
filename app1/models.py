from django.db import models

# Create your models here.
class Film(models.Model):
    name = models.CharField(max_length=255)
    ganre = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    year = models.IntegerField()
    link = models.CharField(max_length=255, default='')
    image = models.ImageField(upload_to='app1/')