from django.http import JsonResponse
from django.shortcuts import render

# third party imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import mixins

from .serializers import PostSerializer
from .models import Post

class PostView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PostCreateView(mixins.ListModelMixin, generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

# class Test_view(APIView):

#     # Create Token - in cmd - python manage.py drf_create_token username

#     permission_classes = (IsAuthenticated, )

#     def get(self, request, *args, **kwargs):
#         ### get request serializ for all instance
#         qs = Post.objects.all()
#         serializer = PostSerializer(qs, many=True)

#         ### get request serializ for one instance
#         #post = qs.first()
#         #serializer = PostSerializer(post)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

# def test_view(request):
#     data = {
#         'name': 'john',
#         'age': 14
#     }
#     return JsonResponse(data)