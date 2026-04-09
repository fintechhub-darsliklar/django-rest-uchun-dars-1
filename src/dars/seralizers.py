from rest_framework.serializers import ModelSerializer
from .models import Universitet


class UniversitetSeralizer(ModelSerializer):

    class Meta:
        model = Universitet
        fields = ['id', 'name', 'is_active']
