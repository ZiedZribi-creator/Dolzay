from django.conf.urls import include 
from django.urls import path
from rest_framework import routers
from .views import ReviewViewSet

router = routers.DefaultRouter()
router.register('review',ReviewViewSet)
urlpatterns=[
    path('',include(router.urls)),
]