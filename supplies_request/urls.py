from django.urls import path
from . import views
urlpatterns = [
	path('pedidos', views.supplies_request, name='supplies_request'),
]