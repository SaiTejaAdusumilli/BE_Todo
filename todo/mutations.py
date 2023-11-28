import graphene

from graphene_django import DjangoObjectType

from .models import todo


class TodoDataType(DjangoObjectType):
    class Meta:
        model = todo
        fields = "__all__"

class TodoMutation(graphene.Mutation):
  class Arguments:
      task = graphene.String(required=True)
      desc = graphene.String(required=True)
      status = graphene.String(required=False)

  ok = graphene.Boolean()
  todo = graphene.Field(TodoDataType)

  def mutate(self, info, task, desc, status="TODO"):
    ok = True
    TODO = todo(task=task, desc=desc, status=status)
    TODO.save()

    return TodoMutation(ok=ok, todo=TODO)

class UpdateTodoMutation(graphene.Mutation):
  class Arguments:
      task = graphene.String(required=False)
      desc = graphene.String(required=False)
      status = graphene.String(required=False)
      id = graphene.Int(required = True)

  ok = graphene.Boolean()
  todo = graphene.Field(TodoDataType)

  def mutate(self, info, id,task, desc, status):
    ok = True
    todo.objects.filter(id=id).update(task=task, desc=desc, status=status)
    TODO = todo.objects.get(id=id)

    return UpdateTodoMutation(ok=ok, todo=TODO)

class DeleteTodoMutation(graphene.Mutation):
  class Arguments:
      id = graphene.Int(required = True)

  ok = graphene.Boolean()
  todo_msg = graphene.String()


  def mutate(self, info, id):
    ok = True
    todo.objects.filter(id=id).delete()
    TODO = f"Deleted Object with id = {id}"

    return DeleteTodoMutation(ok=ok, todo_msg=TODO)

class Mutation(graphene.ObjectType):
    create_todo = TodoMutation.Field()
    update_todo = UpdateTodoMutation.Field()
    delete_todo = DeleteTodoMutation.Field()