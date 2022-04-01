from django.shortcuts import render
from django.http.response import JsonResponse
from stocksapp.models import Stocks
from stocksapp.serializers import StocksSerializer
# Create your views here.


def DispRecords(request,date=""):
    if request.method=='GET':
        stock=Stocks.objects.filter(date=date)
        stock_serializer=StocksSerializer(stock,many=True)
        return JsonResponse(stock_serializer.data,safe=False)