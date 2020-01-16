from django.conf.urls import include 
from django.urls import path
from rest_framework import routers
from .views import ProjectViewSet

router = routers.DefaultRouter()
router.register('project',ProjectViewSet)
urlpatterns=[
    path('',include(router.urls)),
]