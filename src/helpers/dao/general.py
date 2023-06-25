from src.utilities.db_connection import DBConnection
import logging as logger

class GeneralDAO:
    table = None

    db = DBConnection("wowsite")
    
    @classmethod
    def get_item_by_id(cls, id=1, alt_id_name=None):
        id_name = alt_id_name if alt_id_name else "id"
        db_response =  cls.db.execute_select("*", cls.table, f"{id_name} = {id}")[0]
        logger.debug(db_response)
        return db_response
    
    @classmethod
    def get_last_item_in_table(cls):
        db_response = cls.db.execute_select("*", cls.table, order_by="id desc", limit=1)[0]
        logger.debug(db_response)
        return db_response
    
    @classmethod
    def get_all_items(cls):
        db_response = cls.db.execute_select("*", cls.table)
        logger.debug(db_response)
        return db_response
    
    @classmethod
    def delete_item_by_id(cls, id):
        cls.db.execute_delete(cls.table, condition=f"id = {id}")
