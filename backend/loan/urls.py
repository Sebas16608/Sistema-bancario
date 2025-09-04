from django.contrib import admin
from django.urls import path, include
from .views import CreditoView, PagoView, AhorroView, DepositoView

urlpatterns = [
    path("credito/", CreditoView.as_view(), name="credito-list"),
    path("cretido/<int:pk>/", CreditoView.as_view(), name="credito-detail"),
    path("pago/", PagoView.as_view(), name="pago-list"),
    path("pago/<int:pk>/", PagoView.as_view(), name="pago-detail"),
    path("ahorro/", AhorroView.as_view(), name="ahorro-list"),
    path("ahorro/<int:pk>/", AhorroView.as_view(), name="ahorro-detail"),
    path("deposito/", DepositoView.as_view(), name="deposito-list"),
    path("deposito/<int:pk>/", DepositoView.as_view(), name="deposito-detail")
]
