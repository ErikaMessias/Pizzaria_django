from django.urls import include, path
from rest_framework import routers
from .views import PizzariaViewSet

router = routers.DefaultRouter()
router.register(r'pizzaria', PizzariaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]