from rest_framework import serializers
from .models import Code, RedirectURL



class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = "__all__"
        
        
class RedirectURLSerializer(serializers.ModelSerializer):
    base_url = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = RedirectURL
        fields = "__all__"
        