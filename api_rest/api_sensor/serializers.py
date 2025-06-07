from rest_framework import serializers
from .models import SensorData

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'  # Ou defina campos específicos: ['temperatura', 'vibracao', ...]
