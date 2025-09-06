from django.urls import path
from .views import UserView

urlpatterns = [
    path("usuario/", UserView.as_view(), name="usuarios-list"),
    path("usuario/<int:pk>/", UserView.as_view(), name="usuarios-detail")
]