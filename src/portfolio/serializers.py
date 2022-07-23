from rest_framework import serializers
from. models import Portfolio, Category

class Portfolio_serializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'

class Category_serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'