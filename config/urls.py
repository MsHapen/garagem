from django.contrib import admin
from django.urls import include, path

from Garagem.views import VeiculoViewSet, MarcaViewSet, AcessorioViewSet, CorViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()


router.register(r"veiculos", VeiculoViewSet)
router.register(r"marcas", MarcaViewSet)
router.register(r"acessorio", AcessorioViewSet)
router.register(r"cor", CorViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]