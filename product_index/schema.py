import graphene
from graphene_django import DjangoObjectType

from .models import App


class AppType(DjangoObjectType):
    class Meta:
        model = App


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
