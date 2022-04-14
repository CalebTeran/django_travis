from rest_framework import routers
from .views import EditorialViewSet, CompanyViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('company', CompanyViewSet)
router.register('', EditorialViewSet)

urlpatterns = [
	path('', include(router.urls)),
]