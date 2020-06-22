from django.urls import path, include
from .views import EventCreateView, EventRetrieveDestroyUpdateView, EventListView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', EventListView)

urlpatterns = [
    path('create/', EventCreateView.as_view()),
    path('<int:pk>/', EventRetrieveDestroyUpdateView.as_view()),
    path('', include(router.urls))
]
