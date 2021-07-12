from . import models, serializers
from rest_framework import generics, permissions
from rest_framework.response import Response

from django.contrib.auth.models import User


class SignUpView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.ProfileSerializer


class UsersView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.ApiPokemonSerializer
    queryset = models.Profile.objects.all()


class AddPokemonToUser(generics.ListCreateAPIView):
    serializer_class = serializers.PokemonSerializer

    def get_queryset(self):
        return models.Pokemon.objects.all()
