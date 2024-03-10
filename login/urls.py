
from django.contrib import admin
from django.urls import path
from .views import index , logout, protegido,administradores
urlpatterns = [
    path('', index),
    path('logout',logout),
    path('protegido',protegido,name='protegido'),
    path('protegido/administradores',administradores,name='administradores')
]
