from django.urls import path
from .views import EventCreateView, RetrieveView, ListView


urlpatterns = [
    path('create/', EventCreateView.as_view()),
    path('<int:pk>/', RetrieveView.as_view()),
    path('', ListView.as_view({'get': 'list'}))
]
