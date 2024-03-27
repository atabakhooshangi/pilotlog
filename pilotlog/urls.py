from django.urls import path, include
from rest_framework import routers
from .views import ImportExportAPIView

router = routers.DefaultRouter()
router.register(
    prefix='imex',
    viewset=ImportExportAPIView,
    basename='imex'
)

url_patterns = [
    path('', include(router.urls))

]
