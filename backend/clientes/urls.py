from django.urls import path, include
from rest_framework import routers
from clientes import views

router= routers.DefaultRouter()
router.register(r"cliente", views.ClienteView)
router.register(r"contacto", views.ContactoView)
router.register(r"documentos", views.DocView)

urlpatterns = [
    path("", include(router.urls)),
]