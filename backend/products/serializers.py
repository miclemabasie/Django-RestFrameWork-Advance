from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from . import validators
from api.serializers import UserPublicSerializer


class ProductCategorySerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    slug = serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    title = serializers.CharField(validators=[validators.validate_title])
    # user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            "user",
            "id",
            "title",
            "content",
            "price",
            "category",
            "sale_price",
            "discount",
            "url",
        ]

    def get_discount(self, obj):
        if not hasattr(obj, "id"):
            return None
        # or
        if not isinstance(obj, Product):
            return None
        # then
        return obj.get_discount()

    def get_url(self, obj):
        request = self.context.get("request")
        if not request:
            return None
        pk = obj.pk
        return reverse("products:product_detail", kwargs={"pk": pk}, request=request)

    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError("Product with same title already exists")
    #     print(value)
    #     return value

    # def get_user(self, obj):
    #     if not obj.user:
    #         return None
    #     return obj.user.username
