from django.db import models

# Create your models here.

class Products(models.Model):
	name = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=400, blank=True)