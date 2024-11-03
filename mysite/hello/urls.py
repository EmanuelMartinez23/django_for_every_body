from django.urls import include, path
from .views import cookie


urlpatterns = [
        path('',cookie),

        ]
