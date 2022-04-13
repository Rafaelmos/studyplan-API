import psycopg2

import psycopg2

class ConnectBD():
    def __init__(self):
        self.__connect = None

    def get_connect(self):
        if self.__connect is None:
            self.__connect = psycopg2.connect(
                host='localhost',
                database='studyplan',
                user='postgres',
                password='postgres'
            )
        return self.__connect

