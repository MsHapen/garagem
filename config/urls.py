from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from Garagem.views import VeiculoViewSet

router = DefaultRouter()
router.register(r"Veiculos", VeiculoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]