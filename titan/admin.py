from django.contrib import admin

from titan.models import Bon_Livraison_Titan, Commande_Titan

# Register your models here.
store = [Commande_Titan, Bon_Livraison_Titan]
admin.site.register(store)
