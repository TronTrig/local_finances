from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
	path('', views.products, name='products'),
	path('<int:id_product>', views.productDetail, name='product_detail'),
]