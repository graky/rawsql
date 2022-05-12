from django.db import connection
from abstract.utils import DatabaseReader


class LessonReader(DatabaseReader):
    table = 'lesson_lesson'


    def __init__(self, kwargs):
        self.values = ", ".join(map(lambda val: f"'{val}'", kwargs.values()))
        self.keys = ", ".join(kwargs.keys())


    def insert_row(self):
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO {0} ({1}) VALUES ({2}) RETURNING id".format(self.table, self.keys, self.values),)
            row = cursor.fetchone()
            return row[0]


    def delete_row(self):
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM {0} WHERE id = {1} RETURNING id".format(self.table, self.values), )
            row = cursor.fetchone()
            return row[0]
