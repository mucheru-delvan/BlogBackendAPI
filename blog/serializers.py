from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    category = serializers.CharField(
        source="category.name"
    )

    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )

    createdAt = serializers.DateTimeField(
        source="created_at",
        read_only=True
    )

    updatedAt = serializers.DateTimeField(
        source="updated_at",
        read_only=True
    )

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "category",
            "tags",
            "createdAt",
            "updatedAt",
        ]