from .models import Recipe
from rest_framework import serializers

class RecipeSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    category_id = serializers.IntegerField(source='category.id', read_only=True)
    category_ancestor = serializers.CharField(source='category.parent.parent', read_only=True)
    category_parent = serializers.CharField(source='category.parent', read_only=True)
    category_name = serializers.CharField(source='category.title', read_only=True)
    class Meta:
        model = Recipe
        fields = ['title', 'image', 'ingrediant', 'body', 'category_id', 'category_ancestor', 'category_parent', 'category_name']