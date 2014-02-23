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
    sizes = serializers.SerializerMethodField('sizes_to_json')
    colors = serializers.SerializerMethodField('colors_to_json')
    images = serializers.SerializerMethodField('images_to_json')

    class Meta:
        model = Product

    def sizes_to_json(self, obj):
        return json.loads(obj.sizes)
    
    def colors_to_json(self, obj):
        return json.loads(obj.colors)
    
    def images_to_json(self, obj):
        return json.loads(obj.images)
