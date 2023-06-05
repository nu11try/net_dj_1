from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, default='Sensor')


class Measurement(models.Model):
    temperature = models.DecimalField(max_digits=3, decimal_places=1)
    created_at = models.DateTimeField(auto_now=True, )
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE, related_name='measurements')
