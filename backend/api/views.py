from django.shortcuts import render
from django.http import JsonResponse


def api_home(request):
    data = {"message": "This is my django api response"}

    return JsonResponse(data)