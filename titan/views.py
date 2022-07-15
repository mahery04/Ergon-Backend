from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Bon_Livraison_Titan, Commande_Titan
from .serializers import Bon_Livraison_TitanSerializer, Commande_TitanSerializer

#Commande_Titan Begin#


def index(request):
    return HttpResponse("Titan Page")


class Commande_TitanList(APIView):
    def get(self, request):
        query_set = Commande_Titan.objects.all()
        serializer = Commande_TitanSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Commande_TitanSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class Commande_TitanDetail(APIView):
    def get(self, request, id):
        commande = get_object_or_404(Commande_Titan, pk=id)
        serializer = Commande_TitanSerializer(commande)
        return Response(serializer.data)

    def put(self, request, id):
        commande = get_object_or_404(Commande_Titan, pk=id)
        serializer = Commande_TitanSerializer(commande, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        commande = get_object_or_404(Commande_Titan, pk=id)
        commande.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Commande_Titan End#

#Bon_Livraison_Titan Begin#


class Bon_Livraison_TitanList(APIView):
    def get(self, request):
        query_set = Bon_Livraison_Titan.objects.all()
        serializer = Bon_Livraison_TitanSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Bon_Livraison_TitanSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class Bon_Livraison_TitanDetail(APIView):
    def get(self, request, id):
        bl = get_object_or_404(Bon_Livraison_Titan, pk=id)
        serializer = Bon_Livraison_TitanSerializer(bl)
        return Response(serializer.data)

    def put(self, request, id):
        bl = get_object_or_404(Bon_Livraison_Titan, pk=id)
        serializer = Bon_Livraison_TitanSerializer(bl, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        bl = get_object_or_404(Bon_Livraison_Titan, pk=id)
        bl.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Bon_Livraison_Titan End#
