from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KeywordViewSet, FlagViewSet, ContentItemViewSet
from .views import trigger_scan

router = DefaultRouter()
router.register(r'keywords', KeywordViewSet)
router.register(r'flags', FlagViewSet)
router.register(r'content', ContentItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('scan/', trigger_scan, name='trigger-scan'),
]