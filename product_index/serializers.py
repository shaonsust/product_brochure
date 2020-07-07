from .models import *
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'sub_title')


class DiseaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Disease
        fields = ('id', 'name', 'sub_title')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    diseases = DiseaseSerializer(many=True, read_only=True)
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'type', 'description', 'products', 'diseases')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = Groups
        fields = ('id', 'name', 'description', 'type', 'image', 'categories')


class AppDetailSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = App
        fields = ('id', 'name', 'description', 'groups')


class AppListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = App
        fields = ('id', 'name', 'description', 'image')
