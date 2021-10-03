from django.db import models

# Create your models here.

class Product(models.Model):
	name = models.CharField('Nombre', max_length=255, unique=True)
	descripcion = models.CharField('Descripción', max_length=500, blank=True)

	def __str__(self):
		return self.name