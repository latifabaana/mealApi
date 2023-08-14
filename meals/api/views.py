from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import *
from .forms import *

@api_view(['GET'])
def getMeals(request, user_id):
    try:
        meals = Meals.objects.filter(user__id = user_id)
        # pass it through the serializer.
        meals_serialized = MealsSerializer(meals, many= True)
        context = {
            'meals': meals_serialized.data
        }   
    except:
        context = {
            'meals': None
        }
    return Response(context)

@api_view(['DELETE'])
def removeMeal(request, idMeal, user_id):
    try:
        Meals.objects.filter(user__id=user_id,idMeal = idMeal).delete() 
        return Response(status = status.HTTP_200_OK)
    except:
        return Response('That meal is not in the record so cannot be deleted')


@api_view(['POST'])
def postMeals(request):
    # pass it through the form.
    meal_form = MealsForm(request.data)
    # get the user instance corresponding to the id 
    curr_user = User.objects.get(id = request.data['user_id'])

    if meal_form.is_valid():
        new_meal = meal_form.save(commit = False)
        new_meal.user = curr_user
        new_meal.save()
        return Response(status = status.HTTP_201_CREATED)
    else:
        # send the errors. 
        return Response(meal_form.errors)
        

@api_view(['GET'])
def getRoutes(request):
    routes = [
        # change these
        '/api/getMeals'
    ]
    return Response(routes)