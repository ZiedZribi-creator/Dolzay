from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ReviewSerializer
from .models import Review
class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class=ReviewSerializer 
    queryset =Review.objects.all()
# Create your views here.

