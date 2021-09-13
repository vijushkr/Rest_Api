from rest_framework import serializers
from hospitalweb.models import Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'id',
            'name',
        'age',
        'sex',
        'bloodg',
        'disease'
        )