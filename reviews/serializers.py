from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Review 
        fields = ('client_name','content',
                  'image','date','rate',)

# obj = Review.objects.create(data)
# ser = ReviewSerializer(obj,many=False)
# return ser.data 