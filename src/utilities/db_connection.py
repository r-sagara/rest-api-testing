from src.configs.hosts import HOSTS
from src.configs.env_setup import DBkeys, Environment
import logging as logger
import pymysql
from pymysql.cursors import DictCursor
import os

class DBConnection:
    machine = Environment.machine
    assert machine, f"MACHINE variable is empty value"

    env = os.environ.get('ENV', 'test')
    db_auth = DBkeys
    

    def __init__(self) -> None:
        db_host_data = HOSTS[self.machine][self.env]['db']
        self.connection_data = {"host": db_host_data['host'],
                                "port": db_host_data['port'],
                                "user": self.db_auth.user, 
                                "password": self.db_auth.password,
                                "db": db_host_data['name']}

    def execute_sql(self, sql_query):
        connection = pymysql.connect(**self.connection_data)
        logger.debug("Connection to database established")
        cursor = connection.cursor(DictCursor)
        cursor.execute(sql_query)
        logger.debug(f"QUERY: {sql_query}")
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
    
    def execute_delete(self, table, condition=""):
        if condition:
            condition = f"where {condition}"
        query = f"delete from {table} {condition};"
        self.execute_sql(query)

    
