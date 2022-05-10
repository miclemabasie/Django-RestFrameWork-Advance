from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


from products.forms import ProductForm

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    
    data = request.data
    serializer = ProductSerializer(data=data)
    if serializer.is_valid():
        instance = serializer.save()
        print(instance)
        dat = ProductSerializer(instance).data

        print(dat)

        return Response(dat)


def test_form(request):
    if request.method == 'POST':
        from_data = request.POST
        form = ProductForm(data=from_data)
        if form.is_valid():
            print('this form is valid')
        else:
            print('There was an error')

        

