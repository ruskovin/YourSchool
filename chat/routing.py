from django.urls import path

from . import consumers

websocket_urlpatterns = [
  path('ws/room/<room_name>/', consumers.ChatConsumer.as_asgi()), # Using asgi
]