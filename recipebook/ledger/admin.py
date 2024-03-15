# Register your models here.
from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient

class RecipeInLine(admin.StackedInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeInLine,]

class RecipeIngredientInline(admin.StackedInline):  
    model = RecipeIngredient

class IngredientAdmin(admin.ModelAdmin):    
    model = Ingredient

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)

