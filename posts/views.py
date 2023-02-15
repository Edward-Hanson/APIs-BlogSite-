from django.contrib.auth.models import User
from .serializers import PostSerializer, UserSerializer
from .models import Post
from rest_framework import viewsets

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset= Post.objects.all()
    serializer_class = PostSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
