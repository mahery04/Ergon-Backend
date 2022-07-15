from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from customer.serializers import GuestSerializer, ParticulierSerializer, RdvSerializer, SocieteSerializer
from .models import Societe, Particulier, Guest, Rdv


def index(request):
    return HttpResponse("Customer Page")


def customercategorie(request):
    pass
#Societe Begin#


class SocieteList(APIView):
    def get(self, request):
        query_set = Societe.objects.all()
        serializer = SocieteSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SocieteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SocieteDetail(APIView):
    def get(self, request, id):
        societe = get_object_or_404(Societe, pk=id)
        serializer = SocieteSerializer(societe)
        return Response(serializer.data)

    def put(self, request, id):
        societe = get_object_or_404(Societe, pk=id)
        serializer = SocieteSerializer(societe, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        societe = get_object_or_404(Societe, pk=id)
        societe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#Societe End#

#Particulier Begin#


class ParticulierList(APIView):
    def get(self, request):
        query_set = Particulier.objects.all()
        serializer = ParticulierSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ParticulierSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ParticulierDetail(APIView):
    def get(self, request, id):
        particulier = get_object_or_404(Particulier, pk=id)
        serializer = ParticulierSerializer(societe)
        return Response(serializer.data)

    def put(self, request, id):
        particulier = get_object_or_404(Particulier, pk=id)
        serializer = ParticulierSerializer(societe, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        particulier = get_object_or_404(Particulier, pk=id)
        particulier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#Particulier End#

#Guest Begin#


class GuestList(APIView):
    def get(self, request):
        query_set = Guest.objects.all()
        serializer = GuestSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GuestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GuestDetail(APIView):
    def get(self, request, id):
        guest = get_object_or_404(Guest, pk=id)
        serializer = GuestSerializer(guest)
        return Response(serializer.data)

    def put(self, request, id):
        guest = get_object_or_404(Guest, pk=id)
        serializer = ParticulierSerializer(guest, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        guest = get_object_or_404(Guest, pk=id)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#Guest End#

#RDV Begin#


class RdvList(APIView):
    def get(self, request):
        query_set = Rdv.objects.all()
        serializer = RdvSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RdvSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RdvDetail(APIView):
    def get(self, request, id):
        rdv = get_object_or_404(Rdv, pk=id)
        serializer = RdvSerializer(rdv)
        return Response(serializer.data)

    def put(self, request, id):
        rdv = get_object_or_404(Rdv, pk=id)
        serializer = RdvSerializer(rdv, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        rdv = get_object_or_404(Rdv, pk=id)
        rdv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#RDV End#
