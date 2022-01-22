from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
	path('', views.products, name='products'),
	path('<int:id_product>', views.detail, name='product_detail'),
	path('formulario/<int:id_product>/eliminar', views.delete, name='delete_product'),
	path('formulario/<int:id_product>', views.form, name='filled_product_form'),
	path('formulario', views.form, name='product_form'),	
]
