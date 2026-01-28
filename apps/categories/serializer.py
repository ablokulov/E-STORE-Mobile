from rest_framework import serializers

from .models import Category

class CategoriesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        

class CategoriesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields  = ["name"]
            
        