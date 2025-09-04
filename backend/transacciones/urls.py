from django.urls import path, include
from .views import TransaccionView

urlpatterns = [
    path("transaccion/", TransaccionView.as_view(), name="transacciones-list"),
    path("transaccion/<int:pk>", TransaccionView.as_view(), name="trasaccion-detail")
]