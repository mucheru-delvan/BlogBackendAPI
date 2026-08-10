from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet


router = DefaultRouter()

router.register("posts", PostViewSet, basename="posts")


urlpatterns = [
    path("", include(router.urls)),
]