from wsgiref import validate
from rest_framework import serializers
from rest_framework.reverse import reverse
from rest_framework import validators
from .models import Product
from api.validators import validate_title, validated_no_hello_in_title, unique_product_title

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail', 
        lookup_field='pk'
    )
    title = serializers.CharField(validators=[unique_product_title, validated_no_hello_in_title])
    # email = serializers.EmailField(write_only=True, validators=[validators.UniqueValidator])
    class Meta:
        model = Product
        fields = [
            # 'email',
            'url',
            'edit_url',
            'pk',
            'title',
            'content', 
            'price',
            'my_discount'
        ]
    """
        we use the create method to overwrite the way a model instance is created
        Like if we need to remove or add in some context in the data that is needed for creating this model instance
        Like Sending an email or doing any kind of thing that needs to be done in conjunction with the creation of the model instance
    """

    # def create(self, validated_data):
    #     print(validated_data)
    #     email = validated_data.pop('email')
    #     # Send some email function right here
    #     print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@{}'.format(email))
    #     return super().create(validated_data)

    # def validate_title(self, value):
        # qs = Product.objects.filter(title__iexact=value).first()
        # if qs is not None:
        #     raise serializers.ValidationError(f"{value} is already a product name.")
        # return value
        # validators.validate_title(value)

    def get_edit_url(self, obj):
        # return f"api/products/{obj.pk}/"
        request = self.context.get('request')
        if not request:
            return None
        return reverse('product-edit', kwargs={'pk': obj.pk}, request=request)

    def get_my_discount(self, obj):
        if isinstance(obj, Product):
            return obj.get_discount()
        else:
            None
          