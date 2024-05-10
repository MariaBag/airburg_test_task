from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions

from tickets.views import StationViewSet, PassengerViewSet, TicketsViewSet, UserViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="Tickets API",
      default_version='v1',
      description="Test task for Airburg"
   ),
   public=True,
   permission_classes=[permissions.AllowAny,],
)

router = routers.DefaultRouter()
router.register(r'stations', StationViewSet)
router.register(r'passengers', PassengerViewSet)
router.register(r'tickets', TicketsViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
