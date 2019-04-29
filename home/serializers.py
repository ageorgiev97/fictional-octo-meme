from rest_framework.serializers import ModelSerializer
from home.models import Restaurant, Vote, Dish

class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class VoteSerializer(ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'


class DishSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'
