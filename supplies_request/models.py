from django.db import models
from products.models import Product
# Create your models here.

class SuppliesRequest(models.Model):
	date = models.DateField('Fecha')
	provider = models.CharField('Proveedor', max_length=200)

class RequestContent(models.Model):
	id_supplies_request = models.ForeignKey(SuppliesRequest, on_delete=models.CASCADE, verbose_name='Pedido')
	#temporal id_producto have text name of the product
	#will be changed for a id soo
	id_product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto')
	quantity = models.IntegerField('Cantidad')
	cost_d = models.DecimalField('Coste en Dolares',max_digits=15 ,decimal_places=2, default=0)
	cost_b = models.DecimalField('Coste en Bolívares',max_digits=15 ,decimal_places=2, default=0)