from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddleware
import dashboard
from dashboard.routings import websocket_urlpatterns
application = ProtocolTypeRouter({
    'websocket': URLRouter(websocket_urlpatterns)
})