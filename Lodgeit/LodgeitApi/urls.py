from django.urls import path, include
from .views import StaffViewset, CompanyViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Staff', StaffViewset)
router.register('Company', CompanyViewset)

urlpatterns = [
    path('', include(router.urls)),
] + router.urls