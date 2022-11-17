from django.shortcuts import render
from .models import Recipe
from .serializer import RecipeSerializer
from rest_framework import viewsets

class RecipeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer