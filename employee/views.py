from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from employee.serializers import CongeeSerializer, HistoriqueSerializer, PersonnelSerializer, SalaireSerializer
from .models import Congee, Historique, Personnel, Salaire


def index(request):
    return HttpResponse("Employee Page")

#Personnel Begin#


class PersonnelList(APIView):
    def get(self, request):
        query_set = Personnel.objects.all()
        serializer = PersonnelSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonnelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PersonnelDetail(APIView):
    def get(self, request, id):
        personnel = get_object_or_404(Personnel, pk=id)
        serializer = PersonnelSerializer(personnel)
        return Response(serializer.data)

    def put(self, request, id):
        personnel = get_object_or_404(Personnel, pk=id)
        serializer = PersonnelSerializer(personnel, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        personnel = get_object_or_404(Personnel, pk=id)
        personnel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#Personnel End#

#Congee Begin#


class CongeelList(APIView):
    def get(self, request):
        query_set = Congee.objects.all()
        serializer = CongeeSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CongeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CongeeDetail(APIView):
    def get(self, request, id):
        congee = get_object_or_404(Congee, pk=id)
        serializer = CongeeSerializer(congee)
        return Response(serializer.data)

    def put(self, request, id):
        congee = get_object_or_404(Congee, pk=id)
        serializer = CongeeSerializer(congee, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        congee = get_object_or_404(Congee, pk=id)
        congee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#Congee End#

#Historique Begin#


class HistoriqueList(APIView):
    def get(self, request):
        query_set = Historique.objects.all()
        serializer = HistoriqueSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HistoriqueSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class HistoriqueDetail(APIView):
    def get(self, request, id):
        historique = get_object_or_404(Historique, pk=id)
        serializer = HistoriqueSerializer(historique)
        return Response(serializer.data)

    def put(self, request, id):
        historique = get_object_or_404(Historique, pk=id)
        serializer = HistoriqueSerializer(congee, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        historique = get_object_or_404(Historique, pk=id)
        historique.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#Historique End#

#Salaire Begin#


class SalaireList(APIView):
    def get(self, request):
        query_set = Salaire.objects.all()
        serializer = SalaireSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SalaireSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SalaireDetail(APIView):
    def get(self, request, id):
        salaire = get_object_or_404(Salaire, pk=id)
        serializer = HistoriqueSerializer(salaire)
        return Response(serializer.data)

    def put(self, request, id):
        salaire = get_object_or_404(Salaire, pk=id)
        serializer = SalaireSerializer(congee, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        salaire = get_object_or_404(Salaire, pk=id)
        salaire.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#Salaire End#
