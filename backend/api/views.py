from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from yaml import serialize
from products.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def api_home(request):

    data = request.data
    print(f"this is the data: {data}")
    serializer = ProductSerializer(data=data)


    if serializer.is_valid(raise_exception=True):
        
        serializer.save()
        print(serializer.data)

        return Response({"data": serializer.data})
    return Response({"Error": "invalide data."})


