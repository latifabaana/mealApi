from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('postMeals', views.postMeals , name='postMeals'),
    path('getMeals/<int:user_id>', views.getMeals , name='getMeals'),
    path('removeMeal/<int:user_id>/<int:idMeal>', views.removeMeal , name='removeMeal'),

]