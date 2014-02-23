import json
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Product

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
        
class ProductSerializer(serializers.ModelSerializer):
    sizes = serializers.SerializerMethodField('to_json')
    colors = serializers.SerializerMethodField('to_json')
    images = serializers.SerializerMethodField('to_json')

    class Meta:
        model = Product

    def to_json(self, obj):
        print obj.sizes
        return json.loads(obj.sizes)
