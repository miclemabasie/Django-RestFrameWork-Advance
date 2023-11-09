from django.shortcuts import render
from django.http import JsonResponse
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer
from products.models import Product


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


# def product_list1(request, *args, **kwargs):
#     product = Product.objects.all().order_by("?").first()
#     data = {}
#     data = model_to_dict(product)
#     return JsonResponse(data, safe=False)


# @api_view(["GET"])
# def product_list2(request):
#     product = Product.objects.all().order_by("?").first()
#     data = model_to_dict(product)
#     return Response(data, status=200)


@api_view(["GET"])
def product_detail_view(request):
    product = Product.objects.all().order_by("?").first()
    serializer = ProductSerializer(product)
    data = serializer.data
    return Response(data, status=200)


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
