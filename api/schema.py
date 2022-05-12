import graphene

from .mutation import Mutation

class Query(graphene.ObjectType):
    ...


schema = graphene.Schema(mutation=Mutation)
