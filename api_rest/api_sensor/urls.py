from django.urls import path
from .views import SensorDataOnlyGetView, SensorDataView

urlpatterns = [
    path('receive_data/', SensorDataView.as_view(), name='receive_sensor_data'),
    path('dados-sensores/', SensorDataOnlyGetView.as_view(), name='sensor-data-get-only'),
]
