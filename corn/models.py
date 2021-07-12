import jsonfield
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Profile(models.Model):
    genders = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(choices=genders, max_length=10)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    bio = models.TextField(max_length=124, blank=True)

    def get_pokemon(self):
        return Pokemon.objects.filter(user__id=self.id)

    def __str__(self):
        return f"Profile: {self.user}"


class Pokemon(models.Model):
    name = models.CharField(max_length=54)
    params = jsonfield.JSONField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

# class UserPokemon(models.Model):
#     pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
