from django.urls import path

from .views import SensorView, MeasurementView, SensorViewQ

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('sensors/<pk>/', SensorViewQ.as_view()),
]
