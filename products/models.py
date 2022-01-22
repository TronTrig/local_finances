from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
	name = models.CharField('Nombre', max_length=255, unique=True)
	description = models.CharField('Descripción', max_length=500, blank=True, null=True, db_column='descripcion')

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		#Some day why the below line dont work
		#return  reverse("products:product_detail", kwargs={"id":self.id}) 

		return f"/productos/formulario/{self.id}"
