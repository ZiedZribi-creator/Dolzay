from django.db import models

# Create your models here.
class Brand(models.Model):
    name    =models.CharField(max_length=400)
    logo    =models.ImageField()
    link    =models.CharField(max_length=1000)
    def __str__(self):
        return self.name
