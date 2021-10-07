from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FilesViewSet

router = DefaultRouter()
router.register(r"files", FilesViewSet)

urlpatterns = [
    path("", include(router.urls))
]