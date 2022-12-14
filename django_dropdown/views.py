from django.http import JsonResponse
from django.shortcuts import render

from .models import Car, Model, Order

# Create your views here.


def main_view(request):
    qs = Car.objects.all()
    return render(request, 'django-dropdown/main.html', {'qs':qs})

def traditional_view(request):
    qs1 = Car.objects.all()
    qs2 = Model.objects.all()
    return render(request, 'django-dropdown/t.html', {'qs1':qs1, 'qs2':qs2})

def get_json_car_data(request):
    qs_val = list(Car.objects.values())
    return JsonResponse({'data':qs_val})

def get_json_model_data(request, *args, **kwargs):
    selected_car = kwargs.get('car')
    obj_models = list(Model.objects.filter(car__name=selected_car).values())
    return JsonResponse({'data':obj_models})

def create_order(request):
    if request.POST.get('is_ajax'):
        car = request.POST.get('car')
        car_obj = Car.objects.get(name=car)
        model = request.POST.get('model')
        model_obj = Model.objects.get(name=model, car__name=car_obj.name)
        Order.objects.create(car=car_obj, model=model_obj)
        return JsonResponse({'created': True})
    return JsonResponse({'created': False})