from ossaudiodev import control_names
from rest_framework import generics, mixins, permissions
from yaml import serialize, serialize_all
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import Http404

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # Here we can add some additinal context before saving the instance of the serializer
        # like
        # serializer.save(user=self.request.user)
        data = serializer.validated_data
        title = data.get('title')
        content = data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

product_list_create_api_view = ProductListCreateAPIView.as_view()


# using model mixins
class ProductMixinView(mixins.ListModelMixin, 
                        mixins.RetrieveModelMixin, 
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin,
                        generics.GenericAPIView
                    ):
    """
        In the GenericApiViewMixins we use methods to perform different operations on the model such as list, detail, post, put, delete by defining methods
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


    # The get method
    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        if 'pk' in kwargs.keys():
            print('There is a primary key value in the request headers')
            return self.retrieve(self, request, args, kwargs)
        return self.list(request, *args, **kwargs)

    # handeling the post operations to this model
    def post(self, request, *args, **kwargs):
        print(args, kwargs)
        return self.create(request, args, kwargs)

    # Altering the product creation process
    def perform_create(self, serializer):
        titile = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = 'This is my new content from mixins'
        serializer.save(content=content)

    
    def delete(self, request, *args, **kwargs):
        if 'pk' in kwargs.keys():
            print('Yes')
        return self.destroy(request, args, kwargs)


    def put(self, request, *args, **kwargs):
        if 'pk' in kwargs.keys():
            print('yes we have a pk')
            return self.update(request, args, kwargs)

    def perform_update(self, serializer):
        instance = serializer.save()
        print(serializer.validated_data)
        if instance.content == None:
            instance.content = 'This is an updated content from the mixins'
            instance.save()
        

    




product_mixin_api_view = ProductMixinView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()

    serializer_class = ProductSerializer

product_detail_api_view = ProductDetailAPIView.as_view()


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_list_api_view = ProductListAPIView.as_view()


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


product_update_api_view = ProductUpdateAPIView.as_view()


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    lookup_field = 'pk'

    def perform_destroy(self, instance):
        print('This is where you can do some extra work')
        return super().perform_destroy(instance)

product_delete_api_view = ProductDeleteAPIView.as_view()







@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    
    method = request.method

    if method == 'GET':
        # if there is a pk then it is a detail view
        if pk is not None:
            # get product by pk
            # product = Product.objects.get(pk=pk)
            # if product is None:
            #     return Http404
            product = get_object_or_404(Product, pk=pk)
            serializer = ProductSerializer(product).data
            return Response(serializer)
        # if not pk then it is a list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        print(data)
        return Response(data)

    if method == 'POST':

        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.validated_data
            print(valid_data)
            
            return Response({'message': serializer.data})

