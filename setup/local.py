#!/usr/bin/env python3

import sqlite3


class Local:

    def __init__(self):
        self.connection = sqlite3.connect('main.db',check_same_thread=False)
        self.cursor     = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self,type_,value_,traceback_):
        if self.connection:
            if self.cursor:
                self.cursor.close()
            self.connection.close()

    def create_table(self,name):
        # TODO 0 Sanitize SQL
        self.cursor.execute(
            f"""CREATE TABLE {name}(
                pk PRIMARY KEY INTEGER
            );"""
        )

    def create_tables(self,names):
        for name in names:
            self.create_table(name)

    def add_column(self,table_name,column_name,column_type):
        # TODO 0 Sanitize SQL
        self.cursor.execute(
            f"""ALTER TABLE {name}
                ADD COLUMN {column_name} {column_type};
            )"""
        )

    def add_columns(self,columns):
        for column in columns:
            self.add_column(
                column['table_name'],
                column['column_name'],
                column['column_type']
            )

if __name__ == '__main__':
    schema = {
                'providers': [{
                    'column_name':'name',
                    'column_type':'VARCHAR'
                }]
                'regions': [{
                    'column_name':'name',
                    'column_type':'VARCHAR'
                }]

            }
    local = Local()

