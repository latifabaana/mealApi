from django import forms
from meals.models import *


class MealsForm(forms.ModelForm):
   class Meta: 
      model = Meals
      fields = ('strMeal', 'idMeal', 'strMealThumb')