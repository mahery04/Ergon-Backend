from django.contrib import admin
from .models import Depot, Materiel, Entre_Sortie

# Register your models here.
store = [Depot, Materiel, Entre_Sortie]
admin.site.register(store)
