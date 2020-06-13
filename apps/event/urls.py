from django.urls import path
from .views import EventCreateView, EventRetrieveDestroyView, EventListView


urlpatterns = [
    path('create/', EventCreateView.as_view()),
    path('<int:pk>/', EventRetrieveDestroyView.as_view()),
    path('', EventListView.as_view({'get': 'list'}))
]
