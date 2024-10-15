import os
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from django.shortcuts import render

# Up two folders to serve "site" content
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.join(BASE_DIR, 'site')

# Vista para la raíz
def home(request):
    return render(request, 'home.html')  # Asegúrate de que esta plantilla exista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),                                                                                           
    re_path(r'^site/(?P<path>.*)$', serve,
        {'document_root': SITE_ROOT, 'show_indexes': True},
        name='site_path'
    ),
    path('', home, name='home'),  # Ruta para la URL raíz
]

