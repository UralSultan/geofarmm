from rest_framework import viewsets, filters
from .serializer import FieldSerializers, Field


class FieldViewSet(viewsets.ModelViewSet):
    serializer_class = FieldSerializers
    queryset = Field.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['farmer', 'coulture']

    def get_queryset(self):
        user = self.request.user
        return Field.objects.filter(farmer__name=user)