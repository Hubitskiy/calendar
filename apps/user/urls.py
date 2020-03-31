from django.urls import path, include
from .views import CreateUserView
from djoser import views as djoser_views


urlpatterns = [
    path('create/', CreateUserView.as_view()),
]
