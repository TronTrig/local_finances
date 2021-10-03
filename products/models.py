from django.db import models

# Create your models here.

class Product(models.Model):
	name = models.CharField('Nombre', max_length=200)
	descripcion = models.CharField('Descripción', max_length=400, blank=True)