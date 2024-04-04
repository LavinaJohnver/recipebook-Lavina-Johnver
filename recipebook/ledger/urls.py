from django.urls import path, include
from django.contrib import admin
from .views import index, RecipeListView, RecipeDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='ledger'),
    path('recipes/list', RecipeListView.as_view(), name='list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe_detail')
]

app_name = 'ledger'
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)