from django.contrib import admin

from hahitantsoa.models import Bon_Livraison_Hahitantsoa, Choix_Sol_Hahitantsoa, Commande_Hahitantsoa, Decoration_Hahitantsoa, Draperie_Hahitantsoa, Effet_Sepciaux_Hahitantsoa, Lumieres_Hahitantsoa, Offre_Hahitantsoa, Package_Hahitantsoa, Paiement_Hahitantsoa, Type_Fete_Hahitantsoa

# Register your models here.
store = [Offre_Hahitantsoa, Paiement_Hahitantsoa, Commande_Hahitantsoa, Package_Hahitantsoa, Choix_Sol_Hahitantsoa, Draperie_Hahitantsoa,
         Decoration_Hahitantsoa, Effet_Sepciaux_Hahitantsoa, Lumieres_Hahitantsoa, Type_Fete_Hahitantsoa, Bon_Livraison_Hahitantsoa]
admin.site.register(store)
