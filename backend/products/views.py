from ossaudiodev import control_names
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
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

product_create_api_view = ProductCreateAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()

    serializer_class = ProductSerializer
