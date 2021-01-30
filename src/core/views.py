from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def test_view(request):
    data = {
        'name': 'john',
        'age': 14
    }
    return JsonResponse(data)