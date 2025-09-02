from django.urls import path, include
from rest_framework import routers
from .views import ClienteView

urlpatterns = [
    path("cliente/", ClienteView.as_view(), name="cliente-list"),
    path("cliente/<int:pk>/", ClienteView.as_view, name='cliente-detail')
]