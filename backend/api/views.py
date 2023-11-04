from django.shortcuts import render
from django.http import JsonResponse
import json


def api_home(request, *args, **kwargs):
    data = {}
    try:
        json_data = request.body
    except:
        json_data = None
    data["args"] = kwargs
    data["data"] = json.loads(json_data)
    data["files"] = {}
    data["from"] = "localhost:800"
    data["headers"] = dict(request.headers)

    return JsonResponse(data)
