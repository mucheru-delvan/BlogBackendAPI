from rest_framework import serializers
from .models import Post, Tag, Category


class PostSerializer(serializers.ModelSerializer):

    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )

    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "category",
            "tags",
            "created_at",
            "updated_at",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation["category"] = instance.category.name

        representation["tags"] = [
            tag.name for tag in instance.tags.all()
        ]

        return representation