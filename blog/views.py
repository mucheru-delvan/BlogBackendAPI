from rest_framework.viewsets import ModelViewSet
from django.db.models import Q
from .models import Post
from .serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get_queryset(self):
        queryset = Post.objects.all()
        
        term = self.request.query_params.get("term")
        if term:
            queryset = queryset.filter(
                Q(title__icontains=term) |
                Q(content__icontains=term) | 
                Q(category__name__icontains=term))
        return queryset
