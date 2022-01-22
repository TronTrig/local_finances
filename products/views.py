from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse, Http404
from django.forms import modelform_factory, ModelForm, CharField, TextInput, ValidationError
from .models import Product
from django.utils.translation import gettext_lazy as _

# Create your views here.
def products(request):

	#the next variable typicaly is named 'queryset'
	list_products = Product.objects.order_by('-id')
	context = {
		#and the name on context usualy is "objct_list"
		'list_products': list_products,
		'meta_title': 'Productos',
		'meta_description': 'Lista de productos', 
	}
	return render(request, 'products/products.html', context)
	

	# response = ', '.join(['<br>Producto numero: {}, con nombre:  {}'.format(p.name, p.id) for p in list_products])
	# template = loader.get_template('products/products.html')
	# return HttpResponse(template.render(context, request))


def detail(request, id_product):
	# reponse = 'You are looking at product %s' % id_product
	# try:
	#	product = Product.objects.get(id=id_product)
	# except Product.DoesNotExist as e:
	#	raise Http404('Los detalles del producto no se encuentran... Lo borraste?')

	product = get_object_or_404(Product, id=id_product)
	context = {
		'product': product,
		'meta_title': product.name.title(),
		'meta_description': 'Muestra mas información acerca del producto {}'.format(product.name.title()),
	}
	return render(request, 'products/details.html', context)


# This handling post of form and rendering the form without ModelForm
"""
def form(request):

	if request.method == 'POST':
		name = request.POST.get('name')
		description = request.POST.get('description')

		try:

			Product.objects.create(name=name, description=description)
			msg = 'Guardado'
		except Exception as exception:
			print(exception.__class__.__name__)
			msg= 'Ya existe el producto \'{}\''.format(name)		

	else:
		msg = ''
		

	context = {
		'msg': msg
	}

	return render(request, 'products/form.html', context)
"""



# This's a example of ModelForm without factory 
class ProductForm(ModelForm):
	"""
	name = CharField(
		label="Nombre",
		widget= TextInput(
			attrs={
					'placeholder': 'Nombre de producto'
				}

			)

		)
	"""
	class Meta:
		model= Product
		fields= (
			'name',
			'description'
		)

		widgets= {
			'name': TextInput(
					attrs={
						'placeholder': _('Nombre del producto'),
						'class': 'form-input'
					}
				),
			'description': TextInput(
				attrs={
					'placeholder': _('Descripción del producto'),
					'class': 'form-input'
				}
			)
		}

		labels= {
			'name': _('Nombre'),
			'description': _('Descripción')
		}

	def clean_name(self, *args, **kwargs):
		#this methosd is to validate the product's name

		#get the data name after the default form validation
		name = self.cleaned_data.get('name')
		#then checks the lengths
		if len(name) > 20:
			#raise a error if is nor valid
			raise ValidationError('El nombre es muy largo')
			#return the name to continue further
		return name
"""
		widgets = {
            'name': CharField(attrs={'cols': 80, 'rows': 20}),
        }
"""
	


# This was a form rendered with modelform_factory
# Now use a created ModelForm
def form(request, id_product=False):



	#ProductForm = modelform_factory(Product, fields=('name', 'description'))
	
	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			print(form.cleaned_data)
		else:
			print(form.errors)
	#check if exist a product's id
	elif not id_product == False:
			#and then use it to get a product
			product = get_object_or_404(Product, id=id_product)
		
			#which is used to fill a Model Form with data
			form = ProductForm(request.POST or None, request.FILES or None , instance=product)
	else:
		form = ProductForm()

	context = {
		'form': form,
		'meta_title': _('Formulario De Productos'),
		'meta_description': _('Lugar para agregar o modificar productos'),
		'id_product': id_product,
	}

	return render(request, 'products/form.html', context)


def delete(request, id_product):
	
	if request.method == 'POST':
		product = get_object_or_404(Product, id=id_product)
		print(id_product)
		product.delete()
		return redirect("../")

	context = {

	}

	return render(request, "products/products.html", context)




#Used to render a form and use build-in django validation
"""
class RawForm(forms.Form):
	name= forms.CharField()
	description= form.CharField()
"""