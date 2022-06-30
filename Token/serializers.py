from rest_framework import serializers
from .models import Account,License

class LicenseSer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = ['license','account']

        depth = 1