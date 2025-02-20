from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from clientes.views import ClienteViewSet

router = DefaultRouter()
router.register(r'cliente', ClienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]