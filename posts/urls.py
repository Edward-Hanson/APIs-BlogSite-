from .views import PostViewSet, UserViewSet
from django.urls import path
from rest_framework.routers import SimpleRouter

router= SimpleRouter()
router.register('users',UserViewSet, basename='users')
router.register('',PostViewSet, basename='posts')

urlpatterns= router.urls