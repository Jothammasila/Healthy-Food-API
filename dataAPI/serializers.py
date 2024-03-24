from rest_framework import serializers
from .models import Food

# The serializer will be used to return our model through the API
# The id filed will be automatically added.

class FoodSerializer(serializers.ModelSerializer):
    class Meta: # Metadata describing the model
        model = Food
        fields = ['id', 'Food_Name', 'Glycemic_Index', 'Calories', 'Fiber_Content', 'Suitable_for_Diabetes', 'Suitable_for_Blood_Pressure',]