from .views import ClienteView, ContactoView, DocView, CreditoView, PagoView, AhorroView, DepositoView, UserView, TrasaccionView
from django.urls import path

urlpatterns = [
    path("cliente/", ClienteView.as_view(), name="cliente-list"),
    path("cliente/<int:pk>/", ClienteView.as_view(), name="cliente-detail"),
    path("contacto/", ContactoView.as_view(), name="contacto-list"),
    path("contacto/<int:pk>/", ContactoView.as_view(), name="contacto-detail"),
    path("documento/", DocView.as_view(), name="document-list"),
    path("documento/<int:pk>/", DocView.as_view(), name="document-detail"),
    path("credito/", CreditoView.as_view(), name="credito-list"),
    path("credito/<int:pk>/", CreditoView.as_view(), name="credito-detail"),
    path("pago/", PagoView.as_view(), name="pago-list"),
    path("pago/<int:pk>/", PagoView.as_view(), name="pago-detail"),
    path("ahorro/", AhorroView.as_view(), name="ahorro-list"),
    path("ahorro/<int:pk>/", AhorroView.as_view(), name="ahorro-detail"),
    path("deposito/", DepositoView.as_view(), name="deposito-list"),
    path("deposito/<int:pk>", DepositoView.as_view(), name="deposito-detail"),
    path("user/", UserView.as_view(), name="user-list"),
    path("user/<int:pk>/", UserView.as_view(), name="user-detail"),
    path("transaccion/", TrasaccionView.as_view(), name="transaccion-list"),
    path("transacciones/<int:pk>", TrasaccionView.as_view(), name="transaccion-detail")
]