import os
import sqlite3

DEFAULT_TABLE_NAME = "vinyl_records"

_DEFAULT_SELECT_QUERY = "SELECT * FROM %s"


class DatabaseError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "A Database Error occurred: %s" % self.message


class VKDatabase:
    def __init__(self, database_path, table_name=DEFAULT_TABLE_NAME):
        self._check_init(database_path)
        self.database_path = database_path
        self.db = sqlite3.connect(self.database_path)
        self.table_name = table_name
        self.default_select_query = _DEFAULT_SELECT_QUERY % self.table_name

    def _check_init(self, database_path):
        full_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), database_path)
        try:
            size = os.path.getsize(full_path)
            if not size:
                raise DatabaseError("database file size is %i" % size)
        except os.error as e:
            raise DatabaseError(e.message)

    def _execute_query(self, query, params=()):
        cursor = self.db.cursor()
        cursor.execute(query, params)
        return self._records_list_to_objects(cursor.fetchall())

    def _records_list_to_objects(self, records_list):
        objects = []
        for item in records_list:
            record = {
                'id': item[0],
                'title': item[1],
                'artist': item[2],
                'cover_art_loc': item[3],
                'playcount': item[4]
            }
            objects.append(record)
        return objects

    def get_records(self):
        return self._execute_query(self.default_select_query)

    def get_record_by_title(self, title):
        query = self.default_select_query + " WHERE title=?"
        params = (title,)
        return self._execute_query(query, params)

    def get_record_by_id(self, id):
        query = self.default_select_query + " WHERE id=?"
        params = (id,)
        return self._execute_query(query, params)

    def get_records_by_artist(self, artist):
        query = self.default_select_query + " WHERE artist=?"
        params = (artist,)
        return self._execute_query(query, params)
