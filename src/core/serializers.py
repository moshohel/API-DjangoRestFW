# Serializer is basically a stacture or representation of model(databases) or form
## It represent the data we want to return or except in json format
### We use serializers to tramsfrom our models to JSON
from rest_framework import serializers

from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title', 'description', 'owner'
        )