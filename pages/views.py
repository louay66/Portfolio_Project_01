from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Category, Guest, Product, Booking
from .Serializer import BookingSerializer, GuestSerializer, ProductSerializer, CategorySerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


class Booking_list(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product', 'guest']


class Booking_delete_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class Product_list(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name', 'price', 'active', 'category']
    search_fields = ['name', 'id', 'price', 'booking']
    ordering_fields = ['price', 'id']
    ordering = ['id']


class Product_delete_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class Category_list(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['new_category', 'product']
    search_fields = ['new_category', 'id']
    ordering_fields = ['new_category', 'id']
    ordering = ['id']


class Category_delete_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class Guest_list(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['first_name', 'last_name', 'phone_number', 'delivery', 'receipt']
    search_fields = ['id', 'first_name', 'last_name', 'phone_number', 'delivery', 'receipt']
    ordering_fields = ['delivery', 'receipt', 'id']
    ordering = ['id']


class Guest_delete_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
