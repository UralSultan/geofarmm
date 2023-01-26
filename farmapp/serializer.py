from rest_framework import serializers
from .models import Field


class FieldSerializers(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ["id",
                  "name",
                  "plot",
                  "farmer",
                  "culture",
                  "seasons",
                  ]
