from django.contrib import admin

from customer.models import Guest, Particulier, Rdv, Societe, Client

# Register your models here.
store = [Societe, Particulier, Guest, Rdv, Client]
admin.site.register(store)
