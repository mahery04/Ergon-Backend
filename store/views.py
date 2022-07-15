from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Depot, Materiel, Entre_Sortie
from .serializers import DepotSerializer, MaterielSerializer, Entre_SortieSerializer

# Create your views here.

#Materiel Begin#


class InventaireList(APIView):
    def get(self, request):
        query_set = Materiel.objects.all()
        serializer = MaterielSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MaterielSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class InventaireDetail(APIView):
    def get(self, request, id):
        materiel = get_object_or_404(Materiel, pk=id)
        serializer = MaterielSerializer(materiel)
        return Response(serializer.data)

    def put(self, request, id):
        materiel = get_object_or_404(Materiel, pk=id)
        serializer = MaterielSerializer(materiel, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        materiel = get_object_or_404(Materiel, pk=id)
        materiel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Materiel End#

#Entree_Sortie Begin#


class Entree_SortieList(APIView):
    def get(self, request):
        query_set = Entre_Sortie.objects.all()
        serializer = Entre_SortieSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Entre_SortieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class Entree_SortieDetail(APIView):
    def get(self, request, id):
        entresortie = get_object_or_404(Entre_Sortie, pk=id)
        serializer = Entre_SortieSerializer(entresortie)
        return Response(serializer.data)

    def put(self, request, id):
        entreesortie = get_object_or_404(Entre_Sortie, pk=id)
        serializer = Entre_SortieSerializer(entreesortie, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        entreesortie = get_object_or_404(Entre_Sortie, pk=id)
        entreesortie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Entree_Sortie End#

#Depot Begin#


class DepotList(APIView):
    def get(self, request):
        query_set = Depot.objects.all()
        serializer = DepotSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DepotSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DepotDetail(APIView):
    def get(self, request, id):
        depot = get_object_or_404(Depot, pk=id)
        serializer = DepotSerializer(depot)
        return Response(serializer.data)

    def put(self, request, id):
        depot = get_object_or_404(Depot, pk=id)
        serializer = DepotSerializer(materiel, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        depot = get_object_or_404(Depot, pk=id)
        depot.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Depot End#
