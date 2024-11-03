from django.urls import include, path
from .views import cookie, sessfun


urlpatterns = [
        path('',sessfun),

        ]
