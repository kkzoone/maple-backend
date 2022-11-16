from django.contrib import admin
from .models import Recipe, Category
from mptt.admin import DraggableMPTTAdmin

class CategoryAdmin(DraggableMPTTAdmin):
    list_display = (
        'tree_actions',
        'indented_title',
        'title',
        'slug',
    )
    mptt_level_indent = 20

admin.site.register(Recipe)
admin.site.register(Category, CategoryAdmin)

