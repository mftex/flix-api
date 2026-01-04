from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from actors.models import Actor
from actors.serializers import ActorSerializer, ActorRetriveUpdateDestroySerializer


class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    
class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Actor.objects.all()
    serializer_class = ActorRetriveUpdateDestroySerializer