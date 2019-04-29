from django.db.models import Model
from django.db.models import CharField, TextField, IntegerField, DecimalField, TimeField, ForeignKey
from django.db.models import CASCADE

from django.contrib.auth.models import AbstractUser

from django.core.validators import MinValueValidator, MaxValueValidator

from djmoney.models.fields import MoneyField
from djmoney.models.validators import MinMoneyValidator

class Restaurant(Model):
    name = CharField(max_length=64)

    description = TextField(max_length=256)

    lunch_start = TimeField('Lunch Start')
    lunch_end = TimeField('Lunch End')

    def __str__(self):
        return self.name

class Dish(Model):
    name = CharField(max_length=64)

    restaurant = ForeignKey(Restaurant, on_delete=CASCADE)
    cost = MoneyField(
        max_digits=6,
        decimal_places=3,
        validators=[MinMoneyValidator(0)]
    )

    calories = IntegerField(
        validators=[MinValueValidator(0)]
    )
    grams = IntegerField(
        validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    def __str__(self):
        return self.email

class Category(Model):
    name = CharField(max_length=64)

    description = TextField(max_length=256)

class Allergen(Model):
    name = CharField(max_length=64)

# Many-to-many relationship tables

class Rating(Model):
    voter = ForeignKey(CustomUser, on_delete=CASCADE)
    restaurant = ForeignKey(Restaurant, on_delete=CASCADE)
    score = IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
    )
    comment = TextField(max_length=256)

    def __str__(self):
        return self.rating

class LikedRestaurants(Model):
    user = ForeignKey(CustomUser, on_delete=CASCADE)
    restaurant = ForeignKey(Restaurant, on_delete=CASCADE)

class RestaurantCategory(Model):
    restaurant = ForeignKey(Restaurant, on_delete=CASCADE)
    category = ForeignKey(Category, on_delete=CASCADE)

class DishAllergen(Model):
    dish = ForeignKey(Restaurant, on_delete=CASCADE)
    allergen = ForeignKey(Allergen, on_delete=CASCADE)
