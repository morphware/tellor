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

    def get_providers(self):
        pass # TODO
        
    def get_services(self,provider):
        pass # TODO
        
    def get_regions(self,provider,service):
        pass # TODO
        


