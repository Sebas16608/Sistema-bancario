from django.urls import path, include
from rest_framework import routers
from .views import ClienteView, ContactoView, DocView
urlpatterns = [
    path("cliente/", ClienteView.as_view(), name="cliente-list"),
    path("cliente/<int:pk>/", ClienteView.as_view(), name='cliente-detail'),
    path("contacto/", ContactoView.as_view(), name="contactos-list"),
    path("contacto/<int:pk>", ContactoView.as_view(), name="contacto-detail"),
    path("documento/", DocView.as_view(), name="documento-list"),
    path("documento/<int:pk>", DocView.as_view(), name="document-detail")
]