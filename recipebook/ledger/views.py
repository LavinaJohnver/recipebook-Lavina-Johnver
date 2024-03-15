from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from ledger.models import Recipe

def index(request):
    return HttpResponse('Recipe Book Ledger')

class RecipeListView(ListView):
	model = Recipe  
	template_name = "recipes_list.html"

class RecipeDetailView(LoginRequiredMixin, DetailView):
	model = Recipe
	template_name = "recipe.html"