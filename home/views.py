from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework.viewsets import ModelViewSet

from home.models import Location, Restaurant, Dish, CustomUser, Category, Allergen, Rating, FavouriteRestaurants, RestaurantCategory, \
    DishAllergen
from home.serializers import LocationSerializer, RestaurantSerializer, DishSerializer, CustomUserSerializer, CategorySerializer, \
    AllergenSerializer, RatingSerializer, FavouriteRestaurantsSerializer, RestaurantCategorySerializer, \
    DishAllergenSerializer
from .forms import CustomUserCreationForm


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class DishViewSet(ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AllergenViewSet(ModelViewSet):
    queryset = Allergen.objects.all()
    serializer_class = AllergenSerializer


class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class FavouriteRestaurantsViewSet(ModelViewSet):
    queryset = FavouriteRestaurants.objects.all()
    serializer_class = FavouriteRestaurantsSerializer


class RestaurantCategoryViewSet(ModelViewSet):
    queryset = RestaurantCategory.objects.all()
    serializer_class = RestaurantCategorySerializer


class DishAllergenViewSet(ModelViewSet):
    queryset = DishAllergen.objects.all()
    serializer_class = DishAllergenSerializer


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
