from django import forms
from .models import Fish

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

class FishForm(forms.ModelForm):
    size = forms.TextInput(attrs={'class': 'form-control'})
    image = forms.ImageField()

    class Meta:
        model = Fish
        fields = ('name', 'model', 'price', 'size', 'color', 'image')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.Select(attrs={'class': 'form-control'}, choices=FISH_MODELS),
            'price': forms.TextInput(attrs={'class': 'form-control'}),

            'color': forms.Select(attrs={'class': 'form-control'}, choices=FISH_COLORS),
        }

