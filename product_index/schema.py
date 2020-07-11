import graphene
from graphene_django import DjangoObjectType

from .models import App, Groups, Category, Product, Disease


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class DiseaseType(DjangoObjectType):
    class Meta:
        model = Disease


class CategoriesType(DjangoObjectType):
    products = ProductType
    diseases = DiseaseType

    class Meta:
        model = Category
        fields = ('id', 'name', 'products', 'diseases')


class GroupType(DjangoObjectType):
    categories = CategoriesType

    class Meta:
        model = Groups
        fields = ('id', 'name', 'type', 'description', 'categories', 'image')


class AppType(DjangoObjectType):
    groups = GroupType

    class Meta:
        model = App
        fields = ('id', 'name', 'description', 'groups', 'image')


class Query(graphene.ObjectType):
    app = graphene.Field(AppType, id=graphene.Int())
    apps = graphene.List(AppType)

    def resolve_app(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return App.objects.get(pk=id)

        return None

    def resolve_apps(self, info, **kwargs):
        return App.objects.all()
