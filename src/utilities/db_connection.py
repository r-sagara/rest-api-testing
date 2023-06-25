from src.configs.hosts import DB_HOSTS, DB_PORT
from src.configs.credentials import DBkeys
import logging as logger
import pymysql
from pymysql.cursors import DictCursor
import os

class DBConnection:
    env = os.environ.get('ENV', 'test')
    db_host = DB_HOSTS[env]
    db_port = DB_PORT[env]
    db_auth = DBkeys

    def __init__(self, database) -> None:
        self.connection_data = {"host": self.db_host,
                                "port": self.db_port,
                                "user": self.db_auth.user, 
                                "password": self.db_auth.password,
                                "db": database}

    def execute_sql(self, sql_query):
        connection = pymysql.connect(**self.connection_data)
        logger.debug("Connection to database established")
        cursor = connection.cursor(DictCursor)
        cursor.execute(sql_query)
        db_response = cursor.fetchall()
        connection.close()
        logger.debug("Connection to database closed")
        return db_response
    
    def execute_select(self, field, table, condition="", order_by="", limit=0):
        if condition:
            condition = f"where {condition}"
        if order_by:
            order_by = f"order by {order_by}"
        limit = f"limit {limit}" if limit else ""
        query = f"select {field} from {table} {condition} {order_by} {limit};"
        return self.execute_sql(query)

    