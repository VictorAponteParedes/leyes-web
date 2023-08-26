
from django.contrib import admin
from django.urls import path, include
from leyes import views
from .views import IndexView ,CrearCasoView, CrearClienteView, CrearAbogadoView, AbogadoDetailView


from setup import settings
from django.conf.urls.static import static


from rest_framework.routers import DefaultRouter


routers = DefaultRouter()

routers.register("casos", views.CasoViewSet, basename="caso")
routers.register("clientes", views.ClienteViewSet, basename="cliente")
routers.register("abogados", views.AbogadoViewSet, basename="abogado")


urlpatterns = [
    #vistas del api
    path('', include(routers.urls)),

    #vistas del cliente
    path('index/', IndexView.as_view(), name='index'),
    path('crear_caso/', CrearCasoView.as_view(), name='crear_caso'),
    path('crear_cliente/', CrearClienteView.as_view(), name='crear_cliente'),
    path('crear_abogado/', CrearAbogadoView.as_view(), name='crear_abogado'),
    # Details
    path('abogado_detalle/<int:pk>/', AbogadoDetailView.as_view(), name='abogado_detail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)

