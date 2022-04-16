from rest_framework import serializers
from .models import Tour


class TourSerializer(serializers.ModelSerializer):


    class Meta:
        fields =( 'customer', 'location', 'date',)
        model = Tour
