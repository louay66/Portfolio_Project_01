from rest_framework import serializers
from rest_framework.serializers import ReadOnlyField
from pages.models import Category, Product, Guest, Booking


class BookingSerializer(serializers.ModelSerializer):
    first_name = ReadOnlyField(source='guest.first_name')
    last_name = ReadOnlyField(source='guest.last_name')
    phone_number = ReadOnlyField(source='guest.phone_number')
    delivery = ReadOnlyField(source='guest.delivery')
    receipt = ReadOnlyField(source='guest.receipt')

    class Meta:
        model = Booking
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'delivery', 'receipt']


class GuestbookSerializer(serializers.ModelSerializer):
    name = ReadOnlyField(source='product.name')
    description = ReadOnlyField(source='product.description')
    price = ReadOnlyField(source='product.price')
    image = ReadOnlyField(source='product.image')

    class Meta:
        model = Booking
        fields = ['id', 'name', 'description', 'price', 'image']


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.new_category')
    booking = BookingSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image', 'active', 'category', 'booking']


class CategorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=False)

    class Meta:
        model = Category
        fields = ['id', 'new_category', 'product']


class GuestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guest
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'delivery', 'receipt']
