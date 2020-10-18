from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views as RecipeViews


router = DefaultRouter()
router.register('tags', RecipeViews.TagViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]
