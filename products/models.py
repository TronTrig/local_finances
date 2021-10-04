from django.db import models

# Create your models here.

class Product(models.Model):
	name = models.CharField('Nombre', max_length=255, unique=True)
	description = models.CharField('Descripción', max_length=500, blank=True, db_column='descripcion')

	def __str__(self):
		return self.name