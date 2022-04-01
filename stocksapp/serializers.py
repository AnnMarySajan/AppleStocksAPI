from rest_framework import serializers
from stocksapp.models import Stocks

class StocksSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stocks
        fields=('date','open','high','low','close','adjclose','volume')