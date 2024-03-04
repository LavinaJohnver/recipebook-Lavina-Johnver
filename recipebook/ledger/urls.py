from django.urls import path, include
from django.contrib import admin
from .views import index, RecipeListView, RecipeDetailView

urlpatterns = [
    path('', index, name='ledger'),
    path('recipes/list', RecipeListView.as_view(), name='list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe_detail')
]

app_name = 'ledger'