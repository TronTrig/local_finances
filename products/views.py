from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.

def products(request):
	list_products = Product.objects.order_by('id')
	response = ', '.join(['<br>Producto numero: {}, con nombre:  {}'.format(p.name, p.id) for p in list_products])
	return HttpResponse(response)

def productDetail(request, product_id):
	reponse = 'You are looking at product %s' % id_product
	return HttpResponse(reponse)