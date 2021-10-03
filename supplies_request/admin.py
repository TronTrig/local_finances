from django.contrib import admin
from .models import SuppliesRequest
from .models import RequestContent
# Register your models here. 

admin.site.register(SuppliesRequest)
admin.site.register(RequestContent)
