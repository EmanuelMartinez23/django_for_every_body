from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('', views.home, name='home'),  # Add this line for the root URL
    path('site/<path:path>/', views.site_path, name='site_path'),
]

