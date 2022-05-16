from rest_framework import viewsets, mixins
from .serializers import ProductSerializer
from .models import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'  # default


# if we want to use viewsets as normal urls
# This helps clarify the the exact paths the urls accepts
product_list_view = ProductViewSet.as_view({'get': 'list'})

product_detail_view = ProductViewSet.as_view({'get': 'retrieve'})


class ProductGenericViewSet(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin, 
                            viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
