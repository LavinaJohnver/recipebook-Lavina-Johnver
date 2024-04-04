from django.contrib import admin
from .models import Recipe, RecipeImage,Ingredient, RecipeIngredient

class RecipeInLine(admin.StackedInline):
    model = RecipeIngredient


class RecipeImageInLine(admin.StackedInline):
    model = RecipeImage


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeInLine,RecipeImageInLine]


class RecipeIngredientInline(admin.StackedInline):  
    model = RecipeIngredient


class IngredientAdmin(admin.ModelAdmin):    
    model = Ingredient


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)

