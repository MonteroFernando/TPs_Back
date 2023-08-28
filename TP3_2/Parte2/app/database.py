import mysql.connector

class DatabaseConnector:
    _connection=None
    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            cls._connection=mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                port='3306',
                password='Nano1984*',
                database='production'
                )
        return cls._connection
    @classmethod
    def execute_query(cls,query,params=None):
        cursor=cls.get_connection().cursor()
        cursor.execute(query,params)
        cursor.commit()
        cls._connection.commit()
        return cursor
    @classmethod
    def fech_one(cls,query,params):
        cursor=cls.get_connection().cursor()
        cursor.execute(query,params)
        return cursor.fetchone()
    @classmethod
    def fetch_all(cls,query,params):
        cursor=cls.get_connection().cursor()
        cursor.execute(query)
        return cursor.fetchall()
    @classmethod
    def close_connection(cls):
        if cls._connection is not None:
            cls._connection.close()
            cls._connection=None
        return cls._connection
