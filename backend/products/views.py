from django.shortcuts import render
from django.forms import model_to_dict
from .models import Product
import json
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer


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
def product_list(request):
    data = {}
    product = Product.objects.get(id=1)
    serializer = ProductSerializer(product)
    data = serializer.data
    return Response(data, status=200)
