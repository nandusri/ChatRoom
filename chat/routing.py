from django.urls import path,re_path
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from . import consumers

websocket_urlpatterns = [
	re_path('ws/chat/(?P<room_name>[^/]+)/', consumers.ChatConsumer),
]
