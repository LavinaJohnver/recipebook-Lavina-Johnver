from django.urls import path
from .views import index, recipe_1, recipe_2, recipes_list

urlpatterns = [
    path('', index, name='ledger'),
    path('recipe/1', recipe_1, name="ledger"),
    path('recipe/2', recipe_2, name="ledger"),
    path('recipes/list', recipes_list, name="list")
]

app_name = 'ledger'