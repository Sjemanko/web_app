from rest_framework import serializers
from .models import Product, ShoppingCart, OrderedItems


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    product_name = serializers.CharField(max_length=100, required=True)
    product_gender = serializers.ChoiceField(
        choices = Product.GENDER,
        required=True
    )
    product_category = serializers.ChoiceField(
        choices = Product.CATEGORIES,
        required=True
    )
    product_sizes = serializers.ChoiceField(
        choices = Product.SIZES,
        required=True
    )
    product_price = serializers.FloatField(
        required=True
    )

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.product_name = validated_data.get('product_name', instance.product_name)
        instance.product_category = validated_data.get('product_category', instance.product_category)
        instance.product_sizes = validated_data.get('product_sizes', instance.product_sizes)
        instance.product_price = validated_data.get('product_price', instance.product_price)
        instance.save()
        return instance
    
    class Meta:
        model = Product
        fields = '__all__'


class ShoppingCartSerializer(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    ordered = serializers.BooleanField() 
    
    class Meta:
        model = ShoppingCart
        fields = '__all__'


class ProductInlineSerializer(serializers.Serializer):
    product_name = serializers.ReadOnlyField()
    product_gender = serializers.ReadOnlyField()
    product_category = serializers.ReadOnlyField()
    product_price = serializers.ReadOnlyField()


class OrderedItemsSerializer(serializers.Serializer):
    shopping_cart = ShoppingCartSerializer(read_only=True)
    product = ProductInlineSerializer(read_only=True)
    quantity = serializers.IntegerField()
    
    class Meta:
        model = OrderedItems
        fields = ['shopping_cart', 'product', 'quantity']


class CartItemsSerializer(serializers.Serializer):
    product = ProductInlineSerializer(read_only=True)
    quantity = serializers.IntegerField()

    class Meta:
        model = OrderedItems
        fields = [ 'product', 'quantity']


class OrderSerializer(serializers.Serializer):
    shopping_cart = serializers.PrimaryKeyRelatedField(queryset=ShoppingCart.objects.all(), required=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(),required=True)
    quantity = serializers.IntegerField(required=True)


    def create(self, validated_data):
        return OrderedItems.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.shopping_cart = validated_data.get('shopping_cart', instance.shopping_cart)
        instance.product = validated_data.get('product', instance.product)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance

        
    
    


