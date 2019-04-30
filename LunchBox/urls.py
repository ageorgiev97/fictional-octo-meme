"""BGLunch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from rest_framework.routers import DefaultRouter

from home.views import LocationViewSet, RestaurantViewSet, DishViewSet, CustomUserViewSet, CategoryViewSet, AllergenViewSet, \
    RatingViewSet, FavouriteRestaurantsViewSet, RestaurantCategoryViewSet, DishAllergenViewSet

router = DefaultRouter()
router.register('locations', LocationViewSet)
router.register('restaurants', RestaurantViewSet)
router.register('dishes', DishViewSet)
router.register('users', CustomUserViewSet)
router.register('categories', CategoryViewSet)
router.register('allergens', AllergenViewSet)
router.register('ratings', RatingViewSet)
router.register('likedrestaurants', FavouriteRestaurantsViewSet)
router.register('restaurantcategories', RestaurantCategoryViewSet)
router.register('dishallergens', DishAllergenViewSet)

urlpatterns = [
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('api/', include(router.urls)),
    # path('api/', include('rest_framework.urls'), name='rest_framework'),
    path('admin/', admin.site.urls),
    path('users/', include('home.urls')),
    path('users', include('django.contrib.auth.urls')),
]
