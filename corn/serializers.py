import requests
import json
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(required=True, source='user.username')
    # email = serializers.EmailField(required=True)
    # password = serializers.CharField(required=True, write_only=True,
    #                                  min_length=8, max_length=32)

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        gender = validated_data['gender'] if 'gender' in validated_data else ""
        bio = validated_data['bio'] if 'bio' in validated_data else ""

        user = User.objects.create_user(username=validated_data['username'],
                                        email=email,
                                        password=password)
        profile = Profile.objects.create(user=user, gender=gender,
                                         email=email, bio=bio)
        validated_data['id'] = profile.id
        validated_data['password'] = "*****"
        return validated_data

    class Meta:
        fields = ['id', 'username', 'email', 'password']
        model = User

    def validate(self, attrs):
        username = attrs['username']
        email = attrs['email']
        if User.objects.filter(email=email):
            raise serializers.ValidationError(
                f"Email {email} already exist")
        if User.objects.filter(username=username):
            raise serializers.ValidationError(
                f"Username {username} already exist")
        return attrs


class PokemonSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        attrs['name'] = attrs['name'].lower()
        pokemon_name = attrs['name']
        response = requests.get(
            f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
        if response.status_code != 200:
            raise serializers.ValidationError(
                f"Pokemon named '{pokemon_name}' does not exist")
        attrs['params'] = json.loads(response.text)
        return attrs

    class Meta:
        fields = '__all__'
        model = Pokemon


class UsersSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        print("ITS ME", attrs)
        return attrs

    class Meta:
        fields = ("username", "first_name", "last_name", "email")
        model = User


class ApiPokemonSerializer(ProfileSerializer):
    pokemon = serializers.SerializerMethodField('get_pokemon')

    def get_pokemon(self, profile: Profile):
        return PokemonSerializer(profile.get_pokemon(), many=True).data
