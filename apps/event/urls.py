from django.urls import path
from .views import EventCreateView, RetrieveView


urlpatterns = [
    path('create/', EventCreateView.as_view()),
    path('<int:pk>/', RetrieveView.as_view())
]