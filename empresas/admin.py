from django.contrib import admin
from .models import SectorActividade, Endereco, Empresa

# Register your models here.
admin.site.register(SectorActividade)
admin.site.register(Endereco)
admin.site.register(Empresa)