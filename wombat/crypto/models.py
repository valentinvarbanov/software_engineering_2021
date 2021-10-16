from django.db import models

from rest_framework import serializers
# Create your models here.

class Currency(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField() # price in USD
    code = models.CharField(max_length=3) # e.g. BTC ETH
    supply = models.PositiveIntegerField(default=10000000) # 10 000 000

    def __str__(self):
        return (self.code + " " + str(self.price))

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ["price", "code", "name"]