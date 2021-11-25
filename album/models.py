from django.db import models

# Create your models here.
class collection(models.Model):
    image=models.ImageField(upload_to="photos")
    name=models.CharField(max_length=100)