from django.db import connection
from abstract.utils import DatabaseReader


class LessonReader(DatabaseReader):
    table = 'lesson_lesson'


    def __init__(self, kwargs):
        self.kwargs = kwargs


    def insert_row(self):
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO {0} (title, subtitle) VALUES (%(title)s, %(subtitle)s) RETURNING id".format(self.table), self.kwargs)
            row = cursor.fetchone()
            return row[0]


    def delete_row(self):
        with connection.cursor() as cursor:
            id = self.kwargs.get("id")
            cursor.execute(
                "DELETE FROM {0} WHERE id = %(id)s RETURNING id".format(self.table), {"id": id})
            row = cursor.fetchone()
            return row[0]
