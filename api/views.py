from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import time
from binance.websocket.spot.websocket_client import SpotWebsocketClient as Client

price = {}
my_client = Client()
my_client.start()

my_client.ticker(id=1, callback=message_handler)

# Create your views here.
def index(request, symbol):
    global price

    # if symbol in price:
    #     return JsonResponse({'price': price[symbol]})
    # else
    #     return JsonResponse({'price': 0})
    return JsonResponse({'price': price})


def message_handler(message):
    global price

    price = message
