from django.urls import path
from nomedoapp.views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', TodoViewSet)
urlpatterns = router.urls


