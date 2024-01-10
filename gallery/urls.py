from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtistViewSet, ArtworkViewSet, ExhibitionViewSet

router = DefaultRouter()

router.register(r'artists', ArtistViewSet)
router.register(r'artworks', ArtworkViewSet)
router.register(r'exhibitions', ExhibitionViewSet)

urlpatterns = [
    path('', include(router.urls))
]