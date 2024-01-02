from rest_framework import serializers
from .models import BaseURL, RedirectURL



class BaseURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseURL
        fields = "__all__"
        
        
class RedirectURLSerializer(serializers.ModelSerializer):
    base_url = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = RedirectURL
        fields = "__all__"
        