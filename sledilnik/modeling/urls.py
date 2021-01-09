from django.urls import path

from . import views

urlpatterns = [
    path('models/', views.models),
    path('predictions/<int:year>-<int:month>-<int:day>/', views.predictions_data),
]
