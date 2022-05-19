from rest_framework import serializers

class UserProductInlineSerializer(serializers.Serializer):
    user = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        read_only=True
    )
    title = serializers.CharField(read_only=True)

class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    # other_products = serializers.SerializerMethodField(read_only=True)

    # def get_other_products(self, obj):
    #     user = obj
    #     my_product_qs = user.product_set.all()[:5]
    #     print('##################33')
    #     print(my_product_qs)
    #     data = UserProductInlineSerializer(my_product_qs, many=True, context=self.context).data
    #     return data