from channels.routing import ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import OriginValidator
from channels.routing import ProtocolTypeRouter, URLRouter
import esp8266.routing

application = ProtocolTypeRouter({
    'websocket':OriginValidator(
     AuthMiddlewareStack(
        URLRouter(
            esp8266.routing.websocket_urlpatterns
        )
    ),
    ['192.168.43.142'],
    # ['*'],
    ),
})
