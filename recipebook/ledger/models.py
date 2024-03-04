from django.db import models
from django.urls import reverse

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    
class Ingredient(models.Model):
    name = models.CharField(max_length=100)

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    recipe = models.ForeignKey(
        Recipe,
        on_delete = models.CASCADE,
        related_name = 'ingredients'
    )  
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete = models.CASCADE,
        related_name = 'recipe',
    )  

