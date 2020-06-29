from django.contrib import admin
from django.urls import path, include
from djoser import views as djoser_views
from apps.user.views import JWTAuthenticationView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/jwt/create/', JWTAuthenticationView.as_view()),
    # path('v1/auth/', include("djoser.urls.jwt")),
    path('v1/auth/me/', djoser_views.UserView.as_view()),
    path('v1/users/', include("user.urls")),
    path('v1/events/', include("event.urls"))
]
