from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse, Http404
from django.forms import modelformset_factory
from .models import Product
# Create your views here.

def products(request):
	list_products = Product.objects.order_by('-id')
	context = {
		'list_products': list_products,
		'meta_title': 'Productos',
		'meta_description': 'Lista de productos', 
	}
	return render(request, 'products/products.html', context)
	

	#response = ', '.join(['<br>Producto numero: {}, con nombre:  {}'.format(p.name, p.id) for p in list_products])
	
	##template = loader.get_template('products/products.html')
	
	##return HttpResponse(template.render(context, request))


def detail(request, id_product):
	##reponse = 'You are looking at product %s' % id_product
	#try:
	#	product = Product.objects.get(id=id_product)
	#except Product.DoesNotExist as e:
	#	raise Http404('Los detalles del producto no se encuentran... Lo borraste?')

	product = get_object_or_404(Product, id=id_product)
	context = {
		'product' : product,
		'meta_title': product.name.title(),
		'meta_description': 'Muestra mas información acerca del producto {}'.format(product.name.title()),
	}
	return render(request, 'products/details.html', context)

def form(request):

	ProductFormSet = modelformset_factory(Product, fields = {'name', 'description'})
	if request.method == 'POST':
		formset = ProductFormSet(request.POST, request.FILES)
		if formset.is_valid():
			formset.save()
	else:
		formset = ProductFormSet()
	context = {
		'formset':formset,
		'meta_title': 'Formulario De Productos',
		'meta_description': 'Lugar para agregar o modificar productos',
	}

	return render(request, 'products/form.html', context)
