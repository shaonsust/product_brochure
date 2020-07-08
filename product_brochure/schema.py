import graphene
import product_index.schema


class Query(product_index.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
