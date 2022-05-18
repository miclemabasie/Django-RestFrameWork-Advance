from itertools import product
from rest_framework import validators, serializers
from products.models import Product


def validate_title(value):
    # Check if product with title already exist
    qs = Product.objects.filter(title__iexact=value).first()
    if qs is not None:
        raise serializers.ValidationError(f"{value} is already a product title.")
    return value

def validated_no_hello_in_title(value):
    if 'hello' in value.lower():
        raise serializers.ValidationError(f"{value} is not allowed as product title.")
    return value


product_qs = Product.objects.all()
unique_product_title = validators.UniqueValidator(product_qs)