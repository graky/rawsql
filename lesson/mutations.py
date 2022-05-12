import graphene
from django.utils.translation import gettext_lazy as _
from lesson.models import LessonReader


class CreateLessonMutation(graphene.Mutation):

    class Arguments:
        title = graphene.String(description=_("Lesson title"))
        subtitle = graphene.String(description=_("Lesson subtitle"))

    success = graphene.Boolean()
    message = graphene.String()
    id = graphene.ID()

    @classmethod
    def mutate(cls, root, info, **kwargs):  # NOQA

        lesson_obj = LessonReader(kwargs)
        id_ = lesson_obj.insert_row()
        return {"success": True, "message": "200", "id": id_}


class DeleteLessonMutation(graphene.Mutation):
    """
    Удаление урока
    """

    class Arguments:
        id = graphene.UUID(required=True, description=_("Lesson ID"))

    success = graphene.Boolean()
    message = graphene.String()
    id = graphene.ID()

    @classmethod
    def mutate(cls, root, info, **kwargs):  # NOQA

        lesson_obj = LessonReader(kwargs)
        id_ = lesson_obj.delete_row()
        return {"success": True, "message": "200", "id": id_}


class LessonMutation(graphene.ObjectType):
    create_lesson = CreateLessonMutation.Field()
    delete_lesson = DeleteLessonMutation.Field()
