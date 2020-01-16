from django.db import models

# Create your models here.
class Contact(models.Model):
    name    =models.CharField(max_length=500)
    email   =models.EmailField()
    subject =models.CharField(max_length=600)
    message =models.TextField()
    def __str__(self):
        return "{name} {email}".format(name=self.name,email=self.email)
        