from django.http import JsonResponse
from django.shortcuts import render

# third party imports
from rest_framework.views import APIView
from rest_framework.response import Response

class Test_view(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name': "jsjdfj",
            'age': 43
        }
        return Response(data)

# def test_view(request):
#     data = {
#         'name': 'john',
#         'age': 14
#     }
#     return JsonResponse(data)