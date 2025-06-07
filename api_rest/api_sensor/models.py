from django.db import models

class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperatura = models.FloatField()
    vibracao = models.FloatField()
    corrente = models.FloatField()
    velocidade = models.IntegerField()
    posicao = models.IntegerField()
    pressao = models.FloatField()
    nivel = models.IntegerField()
    qualidade_ar = models.IntegerField()
    umidade = models.FloatField()
    tensao = models.FloatField()
    fumaca = models.IntegerField()

    def __str__(self):
        return f"Sensor Data {self.id}"
