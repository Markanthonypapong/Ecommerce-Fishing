from django.core.validators import validate_comma_separated_integer_list
from django.db import models


# Create your models here.


FISH_MODELS = [
    ("Spinning Rods", "Spinning Rods"),
    ("Baitcasting Rods", "NBaitcasting Rods"),
    ("Fly Rods", "Fly Rods"),
    ("Surf Rods", "Surf Rods"),
    ("Telescopic Rods", "Telescopic Rods"),
]

FISH_SIZES = [
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
]

FISH_COLORS = [
    ("White", "White"),
    ("Yellow", "Yellow"),
    ("Black", "Black"),
    ("Gray", "Gray"),
    ("Light Yellow", "Light Yellow"),
]


class Fish(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50, choices=FISH_MODELS)
    price = models.IntegerField()
    size = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    color = models.CharField(max_length=20, choices=FISH_COLORS)

    def __str__(self):
        return self.name
