from django.db import models
from products.models import Products
# Create your models here.

class Supplies_Request(models.Model):
	date = models.DateField()
	provider = models.CharField(max_length=200)

class Request_Content(models.Model):
	id_supplies_request = models.ForeignKey(Supplies_Request, on_delete=models.CASCADE)
	#temporal id_producto have text name of the product
	#will be changed for a id soo
	id_product = models.ForeignKey(Products, on_delete=models.CASCADE)
	quantity = models.IntegerField()
	cost = models.DecimalField(max_digits=15 ,decimal_places=2)