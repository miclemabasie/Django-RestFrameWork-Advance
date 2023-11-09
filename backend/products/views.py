from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        content = serializer.validated_data.get("content")
        if content is None:
            content = "Some default product content"
        serializer.save(content=content)
        return super().perform_create(serializer)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = "pk"


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# using function based views


@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        # return a product with the given id

        # Check if product detail is requested
        if pk is not None:
            product = get_object_or_404(Product, pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=200)
        else:
            queryset = Product.objects.all()
            serializer = ProductSerializer(queryset, many=True)
            data = serializer.data
            return Response(data, status=200)

    if method == "POST":
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            print(serializer.validated_data)
            instance = serializer.save()
            if instance.content is None:
                instance.content = instance.title
            return Response(serializer.data, status=201)

    if method == "PUT":
        pass

    if method == "PATCH":
        pass


[
    "COOKIES",
    "FILES",
    "GET",
    "META",
    "POST",
    "__class__",
    "__delattr__",
    "__dict__",
    "__dir__",
    "__doc__",
    "__eq__",
    "__format__",
    "__ge__",
    "__getattribute__",
    "__gt__",
    "__hash__",
    "__init__",
    "__init_subclass__",
    "__iter__",
    "__le__",
    "__lt__",
    "__module__",
    "__ne__",
    "__new__",
    "__reduce__",
    "__reduce_ex__",
    "__repr__",
    "__setattr__",
    "__sizeof__",
    "__str__",
    "__subclasshook__",
    "__weakref__",
    "_current_scheme_host",
    "_encoding",
    "_get_full_path",
    "_get_post",
    "_get_raw_host",
    "_get_scheme",
    "_initialize_handlers",
    "_load_post_and_files",
    "_mark_post_parse_error",
    "_messages",
    "_read_started",
    "_set_content_type_params",
    "_set_post",
    "_stream",
    "_upload_handlers",
    "accepted_types",
    "accepts",
    "body",
    "build_absolute_uri",
    "close",
    "content_params",
    "content_type",
    "csrf_processing_done",
    "encoding",
    "environ",
    "get_full_path",
    "get_full_path_info",
    "get_host",
    "get_port",
    "get_signed_cookie",
    "headers",
    "is_secure",
    "method",
    "parse_file_upload",
    "path",
    "path_info",
    "read",
    "readline",
    "readlines",
    "resolver_match",
    "scheme",
    "session",
    "upload_handlers",
    "user",
]
