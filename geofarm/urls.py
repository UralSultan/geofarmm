from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from farmapp.urls import field_router

router = routers.DefaultRouter()
router.registry.extend(field_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('farmer_reg.urls'))
] + router.urls


