from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to="images", null=True)
    ingrediant = models.JSONField(default=dict)
    body = models.JSONField(default=dict)
    category = TreeForeignKey('Category', on_delete=models.CASCADE, null=True)

#레시피 카테고리
class Category(MPTTModel):
    parent = TreeForeignKey(
        'self', related_name='children', 
        on_delete=models.CASCADE, 
        blank=True, null=True
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=False, editable=False, allow_unicode=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'categories'
        ordering = ['tree_id', 'lft']
    
    class MPTTMeta:
        order_insertion_by = ['title']

