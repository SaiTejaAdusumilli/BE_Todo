import graphene
from graphene_django import DjangoObjectType
from .models import todo

class TodoDataType(DjangoObjectType):
    class Meta:
        model = todo
        fields = "__all__"

class Query(graphene.ObjectType):
    all_todo_data = graphene.List(TodoDataType)
    item_data = graphene.Field(TodoDataType, id=graphene.String(required=True))

    def resolve_all_todo_data(root,info,**kwargs):
        return todo.objects.all().order_by('-id')   

    def resolve_item_data(root, info, id):
        try:
            return todo.objects.get(id=id)
        except todo.DoesNotExist:
            return None