from django.urls import path, include
from rest_framework import routers

from api.views import create_claim, ManagersListViewSet


router_v1 = routers.DefaultRouter()
router_v1.register('managers', ManagersListViewSet, basename='managers')
urlpatterns = [
    path('create_claim', create_claim, name='create_claim'),
    path('', include(router_v1.urls)),
]
