from django.db.models import fields
from rest_framework import serializers
from hahitantsoa.models import Bon_Livraison_Hahitantsoa, Choix_Sol_Hahitantsoa, Commande_Hahitantsoa, Decoration_Hahitantsoa, Draperie_Hahitantsoa, Effet_Sepciaux_Hahitantsoa, Lumieres_Hahitantsoa, Offre_Hahitantsoa, Package_Hahitantsoa, Paiement_Hahitantsoa, Type_Fete_Hahitantsoa


class Offre_HahitantsoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offre_Hahitantsoa
        fields = ['package_Hahitantsoa', 'type_Fete_Hahitantsoa', 'choix_Sol_Hahitantsoa',
                  'draperie_Hahitantsoa', 'decoration_Hahitantsoa', 'lumieres_Hahitantsoa', 'effet_Sepciaux_Hahitantsoa']


class Paiement_HahitantsoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paiement_Hahitantsoa
        fields = ['client', 'total_Payer', 'paiement_Effectuer',
                  'reste_Payer', 'date', ]


class Commande_HahitantsoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande_Hahitantsoa
        fields = ['client', 'date_Event_Debut', 'date_Event_Fin',
                  'paiement', 'husband_Nom', 'husband_Prenom', 'wife_Nom', 'wife_Prenom', 'offre_Hahitantsoa', 'pax', 'package', 'droit_Logistique', 'type_Fete', 'choix_Sol', 'draperie', 'decoration', 'lumiere', 'piste_Lumineuse', 'ciel_Etoile', 'effet_Speciaux']


class Package_HahitantsoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package_Hahitantsoa
        fields = ['salle', 'table', 'set_Couverts',
                  'set_Assiettes', 'set_Verres', 'supplement']


class Choix_Sol_HahitantsoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choix_Sol_Hahitantsoa
        fields = ['nom_sol', 'prix_sol']


class Draperie_HahitantsoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Draperie_Hahitantsoa
        fields = ['nom_drap', 'prix_drap']


class Decoration_HahitantsoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decoration_Hahitantsoa
        fields = ['nom_deco', 'prix_deco']


class Effet_Sepciaux_HahitantsoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Effet_Sepciaux_Hahitantsoa
        fields = ['nom_effet_speciaux',
                  'prix_effet_speciaux', 'disposition']


class Lumieres_HahitantsoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lumieres_Hahitantsoa
        fields = ['nom_lumiere', 'prix_lumiere']


class Type_Fete_HahitantsoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type_Fete_Hahitantsoa
        fields = ['jour']


class Bon_Livraison_HahitantsoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bon_Livraison_Hahitantsoa
        fields = ['commande',
                  'numero_BL', 'date_BL']
