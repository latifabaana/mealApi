from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Meals(models.Model):
    strMeal = models.CharField(max_length=100, blank = False, null = False )
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = False, blank = False)
    idMeal = models.IntegerField(blank = False, null = False )
    strMealThumb = models.CharField(max_length=100, blank = False, null = False )


