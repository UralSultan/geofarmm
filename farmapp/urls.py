from .views import FieldViewSet
from rest_framework.routers import DefaultRouter

field_router = DefaultRouter()
field_router.register("fields", FieldViewSet, basename='fields')

