from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import time
from binance.websocket.spot.websocket_client import SpotWebsocketClient as Client

price_btcusdt = 0
price_ethusdt = 0

def index(request, symbol):
    global price_btcusdt, price_ethusdt
    
    if symbol == 'btcusdt':
        return JsonResponse(price_btcusdt)
    elif symbol == 'ethusdt':
        return JsonResponse(price_ethusdt)
    else:
        return JsonResponse({'price': 0})


def message_handler_btcusdt(message):
    global price_btcusdt
    price_btcusdt = message


def message_handler_ethusdt(message):
    global price_ethusdt
    price_ethusdt = message


price = {}
my_client = Client()
my_client.start()

my_client.ticker(symbol="btcusdt", id=1, callback=message_handler_btcusdt)
my_client.ticker(symbol="ethusdt", id=2, callback=message_handler_ethusdt)