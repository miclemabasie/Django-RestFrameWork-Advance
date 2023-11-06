from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            "title",
            "content",
            "price",
            "sale_price",
            "discount",
        ]

    def get_discount(self, obj):
        if not hasattr(obj, "id"):
            return None
        # or
        if not isinstance(obj, Product):
            return None
        # then
        return obj.get_discount()
