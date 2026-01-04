from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from genres.models import Genre
import json
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from genres.serializers import GenreSerializer


class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
