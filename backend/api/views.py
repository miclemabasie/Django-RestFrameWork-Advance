from django.shortcuts import render
from django.http import JsonResponse
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer


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


@api_view(["POST"])
def api_post(request):
    data = request.data
    # validatng data with restFrameWork
    serializer = ProductSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # print(instance)
        pass
        return Response(serializer.data)
    return Response({"message": "invalid data"}, status=400)
