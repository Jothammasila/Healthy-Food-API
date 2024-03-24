from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Food
from .serializers import FoodSerializer

# For different requet methods use api_views decorators

@api_view(['GET', 'POST'])
def food_list(request, format=None):
    
    # 1. Get all the foods
    # 2. Serialize them
    # 3. Return JSON
    
    if request.method == 'GET':
        food = Food.objects.all()
        serializer = FoodSerializer(food, many=True)
        return Response(serializer.data, status=status.HTTP_302_FOUND)
    
    
    elif request.method == 'POST':
        #Get the data and deserialize it then convert to a database object
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])       
def food_details(request, id, format=None):
        
    try:
        food = Food.objects.get(id=id)
    except:
        Food.DoesNotExist
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = FoodSerializer(food)
        return Response(serializer.data, status=status.HTTP_302_FOUND)
    
    if request.method == 'PUT':
        serializer = FoodSerializer(food, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    if request.method == 'DELETE':
        food.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)