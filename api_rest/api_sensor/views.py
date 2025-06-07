from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SensorDataSerializer
from .models import SensorData  # Certifique-se de importar seu modelo de dados

class SensorDataView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            # Salva os dados no banco
            serializer.save()
            return Response({"status": "success", "message": "Dados recebidos e salvos com sucesso!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SensorDataOnlyGetView(APIView):
    def get(self, request, *args, **kwargs):
        sensordata = SensorData.objects.all()
        serializer = SensorDataSerializer(sensordata, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)