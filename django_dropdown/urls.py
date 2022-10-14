from django.urls import path

from . import views

app_name = 'django-dropdown'

urlpatterns = [
    path('', views.main_view, name='main-view'),
    path('t/', views.traditional_view, name='t-view'),
    path('cars-json/', views.get_json_car_data, name='cars-json'),
    path('models-json/<str:car>/', views.get_json_model_data, name='models-json'),
    path('create/', views.create_order, name='create-order'),
]
