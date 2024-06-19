from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Foodtype, Food
from . import forms

import json

# Create your views here.
def manage(request):
    return render(request, 'manage/manage.html')

@csrf_exempt
def foods(request):
    if request.method == "GET":
        foods = Food.objects.all()
        food_types = Foodtype.objects.all()
        food_form = forms.FoodForm()
        food_type_form = forms.FoodtypeForm()
        return render(request, 'manage/foods.html', {
            'food_form': food_form,
            'food_type_form': food_type_form,
            'foods': foods,
            'food_types': food_types,
        })
    elif request.method == "POST":
        form_food = forms.FoodForm(request.POST)
        form_food_type = forms.FoodtypeForm(request.POST)

        if form_food.is_valid():
            data = form_food.cleaned_data
            form_food.save()
            return HttpResponse(json.dumps({
                'status': 'OK',
            }))
        elif form_food_type.is_valid():
            form_food_type.save()
            return HttpResponse(json.dumps({
                'status': 'OK',
            }))
        else:
            return HttpResponse(json.dumps({
                'status': 'FAIL',
            }))

def orders(request):
    return render(request, 'manage/orders.html')

def staffs(request):
    return render(request, 'manage/staffs.html')