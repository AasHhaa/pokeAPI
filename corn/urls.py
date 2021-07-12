from django.urls import path
from rest_framework.authtoken import views as view
from . import views

urlpatterns = [
    path("auth/sign-up/", views.SignUpView.as_view()),
    path("auth/token/", view.obtain_auth_token, name='token-auth'),
    path("pokemon/", views.AddPokemonToUser.as_view()),
    path("users/", views.UsersView.as_view())
]
