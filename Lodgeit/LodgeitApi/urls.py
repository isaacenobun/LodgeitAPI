from django.urls import path, include
from .views import StaffViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Staff', StaffViewset)

urlpatterns = [
    path('', include(router.urls)),
] + router.urls