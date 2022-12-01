from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    product_name = serializers.CharField(max_length=100)
    product_gender = serializers.ChoiceField(
        choices = Product.GENDER,
        default = Product.GENDER[0]
    )
    product_category = serializers.ChoiceField(
        # max_length = 20,
        choices = Product.CATEGORIES
    )
    product_sizes = serializers.ChoiceField(
        # max_length = 2,
        choices = Product.SIZES
    )

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.product_name = validated_data.get('product_name', instance.product_name)
        instance.product_category = validated_data.get('product_category', instance.product_category)
        instance.product_sizes = validated_data.get('product_sizes', instance.product_sizes)
        instance.save()
        return instance