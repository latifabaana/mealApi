from rest_framework import serializers
from meals.models import *
from django.contrib.auth import get_user_model

class MealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meals
        fields = ('strMeal', 'idMeal', 'strMealThumb')