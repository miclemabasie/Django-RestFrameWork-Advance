from rest_framework import validators
from .models import Product


def validate_title(data):
    qs = Product.objects.filter(title__iexact=data)
    if qs.exists():
        raise validators.ValidationError("Product with same name already exist")
    return data
