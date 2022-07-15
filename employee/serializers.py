from django.db.models import fields
from rest_framework import serializers
from employee.models import Congee, Historique, Personnel, Salaire


class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = ['Nom', 'Prenoms', 'Date_naissance',
                  'Lieu_naissance', 'CIN', 'CIN_date_delivrance', 'CIN_recto', 'CIN_verso', 'Certificat_residence', 'Lieu_residence', 'Contact1', 'Contact2', 'Email']


class CongeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Congee
        fields = ['Salarie', 'jour_congé', 'date_congé']


class HistoriqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historique
        fields = ['Salarie', 'date_recrutement', 'date_demission']


class SalaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salaire
        fields = ['Salarie', 'salaire', 'avance']
