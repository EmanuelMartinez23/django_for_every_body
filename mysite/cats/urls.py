from django.urls import include, path, re_path
from . import views 
urlpatterns = [
    path('', views.CatList.as_view(), name='all'),
    path('main/create/', views.CatCreate.as_view(), name='cat_create'),
    path('main/<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),
]
