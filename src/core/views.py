from django.http import JsonResponse
from django.shortcuts import render

# third party imports
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PostSerializer
from .models import Post


class Test_view(APIView):
    def get(self, request, *args, **kwargs):
        ### get request serializ for all instance
        qs = Post.objects.all()
        serializer = PostSerializer(qs, many=True)

        ### get request serializ for one instance
        #post = qs.first()
        #serializer = PostSerializer(post)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# def test_view(request):
#     data = {
#         'name': 'john',
#         'age': 14
#     }
#     return JsonResponse(data)