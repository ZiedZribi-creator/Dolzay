from django.db import models

# Create your models here.
class Review(models.Model):
    client_name =models.CharField(max_length=400) #max length required
    content     =models.TextField ()
    image       =models.ImageField(blank=True,null=True)
    date        =models.DateField(blank=True,null=True)
    rate        =models.IntegerField(default=0)
    def __str__(self): 
        return self.client_name
