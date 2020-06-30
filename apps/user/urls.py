from django.urls import path
from .views import CreateUserView, JWTAuthenticationView


urlpatterns = [
    path('create/', CreateUserView.as_view()),
    path('jwt/create/', JWTAuthenticationView.as_view())
]
