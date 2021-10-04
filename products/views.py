from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Product
# Create your views here.

def products(request):
	list_products = Product.objects.order_by('-id')
	context = {
		'list_products': list_products,
	}
	return render(request, 'products/products.html', context)
	

	#response = ', '.join(['<br>Producto numero: {}, con nombre:  {}'.format(p.name, p.id) for p in list_products])
	
	##template = loader.get_template('products/products.html')
	
	##return HttpResponse(template.render(context, request))


def productDetail(request, id_product):
	##reponse = 'You are looking at product %s' % id_product
	#try:
	#	product = Product.objects.get(id=id_product)
	#except Product.DoesNotExist as e:
	#	raise Http404('Los detalles del producto no se encuentran... Lo borraste?')

	product = get_object_or_404(Product, id=id_product)
	context = {
		'product' : product
	}
	return render(request, 'products/details.html', context)
