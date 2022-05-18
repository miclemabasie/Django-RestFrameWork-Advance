from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail', 
        lookup_field='pk'
    )
    class Meta:
        model = Product
        fields = [
            'url',
            'edit_url',
            'pk',
            'title',
            'content', 
            'price',
            'my_discount'
        ]

    def get_edit_url(self, obj):
        # return f"api/products/{obj.pk}/"
        request = self.context.get('request')
        print(request)
        if not request:
            return None
        return reverse('product-edit', kwargs={'pk': obj.pk}, request=request)

    def get_my_discount(self, obj):
        if isinstance(obj, Product):
            return obj.get_discount()
        else:
            None
          