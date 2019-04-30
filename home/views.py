from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework.viewsets import ModelViewSet

from home.models import Restaurant, Dish, CustomUser, Category, Allergen, Rating, LikedRestaurants, RestaurantCategory, \
    DishAllergen
from home.serializers import RestaurantSerializer, DishSerializer, CustomUserSerializer, CategorySerializer, \
    AllergenSerializer, RatingSerializer, LikedRestaurantsSerializer, RestaurantCategorySerializer, \
    DishAllergenSerializer
from .forms import CustomUserCreationForm


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


class LikedRestaurantsViewSet(ModelViewSet):
    queryset = LikedRestaurants.objects.all()
    serializer_class = LikedRestaurantsSerializer


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
