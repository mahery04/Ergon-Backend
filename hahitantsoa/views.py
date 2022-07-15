from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from hahitantsoa.serializers import Bon_Livraison_HahitantsoaSerializer, Choix_Sol_HahitantsoaSerializer, Commande_HahitantsoaSerializer, Decoration_HahitantsoaSerializer, Draperie_HahitantsoaSerializer, Effet_Sepciaux_HahitantsoaSerializer, Lumieres_HahitantsoaSerializer, Offre_HahitantsoaSerializer, Package_HahitantsoaSerializer, Paiement_HahitantsoaSerializer, Type_Fete_HahitantsoaSerializer
from .models import Bon_Livraison_Hahitantsoa, Choix_Sol_Hahitantsoa, Commande_Hahitantsoa, Decoration_Hahitantsoa, Draperie_Hahitantsoa, Effet_Sepciaux_Hahitantsoa, Lumieres_Hahitantsoa, Offre_Hahitantsoa, Package_Hahitantsoa, Paiement_Hahitantsoa, Type_Fete_Hahitantsoa


def index(request):
    return HttpResponse("Hahitantsoa Page")

# Offre_Hahitantsoa Begin#


class Offre_HahitantsoaList(APIView):
    def get(self, request):
        query_set = Offre_Hahitantsoa.objects.all()
        serializer = Offre_HahitantsoaSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Offre_HahitantsoaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class Offre_HahitantsoaDetail(APIView):
    def get(self, request, id):
        offre = get_object_or_404(Offre_Hahitantsoa, pk=id)
        serializer = Offre_HahitantsoaSerializer(personnel)
        return Response(serializer.data)

    def put(self, request, id):
        offre = get_object_or_404(Offre_Hahitantsoa, pk=id)
        serializer = Offre_HahitantsoaSerializer(offre, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        offre = get_object_or_404(Offre_Hahitantsoa, pk=id)
        offre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#Offre_Hahitantsoa End#


# Paiement_Hahitantsoa Begin#


class Paiement_HahitantsoaList(APIView):
    def get(self, request):
        query_set = Paiement_Hahitantsoa.objects.all()
        serializer = Paiement_HahitantsoaSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Paiement_HahitantsoaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class Paiement_HahitantsoaDetail(APIView):
    def get(self, request, id):
        paiement = get_object_or_404(Paiement_Hahitantsoa, pk=id)
        serializer = Paiement_HahitantsoaSerializer(paiement)
        return Response(serializer.data)

    def put(self, request, id):
        paiement = get_object_or_404(Paiement_Hahitantsoa, pk=id)
        serializer = Offre_HahitantsoaSerializer(paiement, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        paiement = get_object_or_404(Paiement_Hahitantsoa, pk=id)
        paiement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#Paiement_Hahitantsoa End#


# Commande_Hahitantsoa Begin#


class Commande_HahitantsoaList(APIView):
    def get(self, request):
        query_set = Commande_Hahitantsoa.objects.all()
        serializer = Commande_HahitantsoaSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Commande_HahitantsoaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class Commande_HahitantsoaDetail(APIView):
    def get(self, request, id):
        commande = get_object_or_404(Commande_Hahitantsoa, pk=id)
        serializer = Commande_HahitantsoaSerializer(commande)
        return Response(serializer.data)

    def put(self, request, id):
        commande = get_object_or_404(Commande_Hahitantsoa, pk=id)
        serializer = Commande_HahitantsoaSerializer(
            commande, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        commande = get_object_or_404(Commande_Hahitantsoa, pk=id)
        commande.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#Commande_Hahitantsoa End#


# Package_Hahitantsoa Begin#


class Package_HahitantsoaList(APIView):
    def get(self, request):
        query_set = Paiement_Hahitantsoa.objects.all()
        serializer = Package_HahitantsoaSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Package_HahitantsoaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class Package_HahitantsoaDetail(APIView):
    def get(self, request, id):
        package = get_object_or_404(Package_Hahitantsoa, pk=id)
        serializer = Package_HahitantsoaSerializer(package)
        return Response(serializer.data)

    def put(self, request, id):
        package = get_object_or_404(Package_Hahitantsoa, pk=id)
        serializer = Package_HahitantsoaSerializer(package, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        package = get_object_or_404(Package_Hahitantsoa, pk=id)
        package.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#Package_Hahitantsoa End#


# Choix_Sol_Hahitantsoa Begin#


class Choix_Sol_HahitantsoaList(APIView):
    def get(self, request):
        query_set = Choix_Sol_Hahitantsoa.objects.all()
        serializer = Choix_Sol_HahitantsoaSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Choix_Sol_HahitantsoaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class Choix_Sol_HahitantsoaDetail(APIView):
    def get(self, request, id):
        choixsol = get_object_or_404(Choix_Sol_Hahitantsoa, pk=id)
        serializer = Choix_Sol_HahitantsoaSerializer(choixsol)
        return Response(serializer.data)

    def put(self, request, id):
        choixsol = get_object_or_404(Choix_Sol_Hahitantsoa, pk=id)
        serializer = Choix_Sol_HahitantsoaSerializer(
            choixsol, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        choixsol = get_object_or_404(Choix_Sol_Hahitantsoa, pk=id)
        choixsol.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#Choix_Sol_Hahitantsoa End#


# Draperie_Hahitantsoa Begin#


class Draperie_HahitantsoaList(APIView):
    def get(self, request):
        query_set = Draperie_Hahitantsoa.objects.all()
        serializer = Draperie_HahitantsoaSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Draperie_Hahitantsoa(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class Draperie_HahitantsoaDetail(APIView):
    def get(self, request, id):
        draperie = get_object_or_404(Draperie_Hahitantsoa, pk=id)
        serializer = Draperie_HahitantsoaSerializer(draperie)
        return Response(serializer.data)

    def put(self, request, id):
        draperie = get_object_or_404(Draperie_Hahitantsoa, pk=id)
        serializer = Draperie_HahitantsoaSerializer(
            draperie, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        draperie = get_object_or_404(Draperie_Hahitantsoa, pk=id)
        draperie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#Draperie_Hahitantsoa End#

# Decoration_Hahitantsoa Begin#


class Decoration_HahitantsoaList(APIView):
    def get(self, request):
        query_set = Decoration_Hahitantsoa.objects.all()
        serializer = Decoration_HahitantsoaSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Decoration_HahitantsoaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class Decoration_HahitantsoaDetail(APIView):
    def get(self, request, id):
        deco = get_object_or_404(Decoration_Hahitantsoa, pk=id)
        serializer = Decoration_HahitantsoaSerializer(deco)
        return Response(serializer.data)

    def put(self, request, id):
        deco = get_object_or_404(Decoration_Hahitantsoa, pk=id)
        serializer = Decoration_HahitantsoaSerializer(deco, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        deco = get_object_or_404(Decoration_Hahitantsoa, pk=id)
        deco.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#Decoration_Hahitantsoa End#


# Effet_Sepciaux_Hahitantsoa Begin#


class Effet_Sepciaux_HahitantsoaList(APIView):
    def get(self, request):
        query_set = Effet_Sepciaux_Hahitantsoa.objects.all()
        serializer = Effet_Sepciaux_HahitantsoaSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Effet_Sepciaux_HahitantsoaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class Effet_Sepciaux_HahitantsoaDetail(APIView):
    def get(self, request, id):
        effet = get_object_or_404(Effet_Sepciaux_Hahitantsoa, pk=id)
        serializer = Effet_Sepciaux_HahitantsoaSerializer(effet)
        return Response(serializer.data)

    def put(self, request, id):
        effet = get_object_or_404(Effet_Sepciaux_Hahitantsoa, pk=id)
        serializer = Effet_Sepciaux_HahitantsoaSerializer(
            effet, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        effet = get_object_or_404(Effet_Sepciaux_Hahitantsoa, pk=id)
        effet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#Effet_Sepciaux_Hahitantsoa End#


# Lumieres_Hahitantsoa Begin#


class Lumieres_HahitantsoaList(APIView):
    def get(self, request):
        query_set = Lumieres_Hahitantsoa.objects.all()
        serializer = Lumieres_HahitantsoaSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Lumieres_HahitantsoaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class Lumieres_HahitantsoaDetail(APIView):
    def get(self, request, id):
        lumiere = get_object_or_404(Lumieres_Hahitantsoa, pk=id)
        serializer = Lumieres_HahitantsoaSerializer(lumiere)
        return Response(serializer.data)

    def put(self, request, id):
        lumiere = get_object_or_404(Lumieres_Hahitantsoa, pk=id)
        serializer = Lumieres_HahitantsoaSerializer(lumiere, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        lumiere = get_object_or_404(Lumieres_Hahitantsoa, pk=id)
        lumiere.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#Lumieres_Hahitantsoa End#


# Type_Fete_Hahitantsoa Begin#


class Type_Fete_HahitantsoaList(APIView):
    def get(self, request):
        query_set = Type_Fete_Hahitantsoa.objects.all()
        serializer = Type_Fete_HahitantsoaSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Type_Fete_HahitantsoaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class Type_Fete_HahitantsoaDetail(APIView):
    def get(self, request, id):
        typefete = get_object_or_404(Type_Fete_Hahitantsoa, pk=id)
        serializer = Type_Fete_HahitantsoaSerializer(typefete)
        return Response(serializer.data)

    def put(self, request, id):
        typefete = get_object_or_404(Type_Fete_Hahitantsoa, pk=id)
        serializer = Type_Fete_HahitantsoaSerializer(
            typefete, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        typefete = get_object_or_404(Type_Fete_Hahitantsoa, pk=id)
        typefete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#Type_Fete_Hahitantsoa End#


# Bon_Livraison_Hahitantsoa Begin#


class Bon_Livraison_HahitantsoaList(APIView):
    def get(self, request):
        query_set = Bon_Livraison_Hahitantsoa.objects.all()
        serializer = Bon_Livraison_HahitantsoaSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Bon_Livraison_HahitantsoaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class Bon_Livraison_HahitantsoaDetail(APIView):
    def get(self, request, id):
        bl = get_object_or_404(Bon_Livraison_Hahitantsoa, pk=id)
        serializer = Bon_Livraison_HahitantsoaSerializer(bl)
        return Response(serializer.data)

    def put(self, request, id):
        bl = get_object_or_404(Bon_Livraison_Hahitantsoa, pk=id)
        serializer = Bon_Livraison_HahitantsoaSerializer(bl, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        bl = get_object_or_404(Bon_Livraison_Hahitantsoa, pk=id)
        bl.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#Bon_Livraison_Hahitantsoa End#
