from .models import Food, Foodtype
from django import forms

class FoodtypeForm(forms.ModelForm):
    class Meta:
        model = Foodtype
        fields = "__all__"

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = "__all__"