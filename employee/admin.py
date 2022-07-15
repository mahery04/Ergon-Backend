from django.contrib import admin

from employee.models import Congee, Historique, Personnel, Salaire

# Register your models here.
store = [Personnel, Congee, Historique, Salaire]
admin.site.register(store)
