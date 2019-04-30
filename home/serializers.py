from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.viewsets import ModelViewSet

from home.models import Location, Restaurant, Dish, CustomUser, Category, Allergen, Rating, FavouriteRestaurants, RestaurantCategory, \
    DishAllergen


class LocationSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Location
        field = '__all__'


class RestaurantSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class DishSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'


class CustomUserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class CategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AllergenSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Allergen
        fields = '__all__'


class RatingSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class FavouriteRestaurantsSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = FavouriteRestaurants
        fields = '__all__'


class RestaurantCategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = RestaurantCategory
        fields = '__all__'


class DishAllergenSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = DishAllergen
        fields = '__all__'

