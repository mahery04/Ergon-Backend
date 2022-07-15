from rest_framework import serializers
from store.models import Depot, Entre_Sortie, Materiel


class MaterielSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materiel
        fields = ['Designation', 'Emplacement', 'Code', 'Section', 'Quantite',
                  'PrixDAchat', 'PrixDeLocation', 'PrixDeCasse', 'Consigne']


class Entre_SortieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entre_Sortie
        fields = ['Date_Sortie', 'Date_Entree', 'Magasinier']


class DepotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depot
        fields = ['Lieux']
