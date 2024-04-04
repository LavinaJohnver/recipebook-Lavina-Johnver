from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Recipe, RecipeImage,Ingredient, RecipeIngredient, Profile

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


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [
        ProfileInline
    ]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)

