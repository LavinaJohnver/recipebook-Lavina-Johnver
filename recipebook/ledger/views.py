from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from ledger.models import Recipe
from .forms import RecipeForm, RecipeImageForm
from .models import Recipe, RecipeImage

def index(request):
    return HttpResponse('Recipe Book Ledger')

class RecipeListView(ListView):
    model = Recipe  
    template_name = "recipes_list.html"

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipe.html"
    redirect_field_name = "/recipes/list"

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipe_create.html"

class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    template_name = "recipe_add_image.html"
    form_class = RecipeImageForm

    def get_success_url(self):
        return reverse_lazy("ledger:recipe_detail", kwargs={"pk": self.object.recipe.pk})

    def form_valid(self, form):
        form.instance.recipe = Recipe.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)
