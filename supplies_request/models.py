from django.db import models
from products.models import Product
# Create your models here.

class SuppliesRequest(models.Model):
	date = models.DateField('Fecha')
	provider = models.CharField('Proveedor', max_length=255)

	def __str__(self):
		return '{} pedido a {} numero de pedido {}'.format(self.date, self.provider, self.id)

class RequestContent(models.Model):
	id_supplies_request = models.ForeignKey(SuppliesRequest, on_delete=models.CASCADE, verbose_name='Pedido')
	id_product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto')
	quantity = models.IntegerField('Cantidad')
	cost_d = models.DecimalField('Coste en Dolares',max_digits=15 ,decimal_places=2, default=0)
	cost_b = models.DecimalField('Coste en Bolívares',max_digits=15 ,decimal_places=2, default=0)

	def __str__(self):
		return 'numero de pedido {} pedido el {} a {}: {} cantidad {}'.format(self.id_supplies_request.id ,self.id_supplies_request.date, self.id_supplies_request.provider, self.id_product.name, self.quantity)