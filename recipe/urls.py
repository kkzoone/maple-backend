from django.urls import path, include
from .views import RecipeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', RecipeViewSet)

urlpatterns =[
    path('', include(router.urls))
]