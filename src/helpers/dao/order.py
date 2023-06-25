from src.helpers.dao.general import GeneralDAO
import logging as logger

class OrderDAO(GeneralDAO):
    table = "wp_wc_order_stats"
    items_table = "wp_woocommerce_order_items"
    items_details_table = "wp_woocommerce_order_itemmeta"

    @classmethod
    def get_line_items_by_order_id(cls, order_id):
        db_response = cls.db.execute_select("*", cls.items_table, condition=f"order_id = {order_id}")
        logger.debug(db_response)
        return db_response
    
    @classmethod
    def get_line_item_details_by_item_id(cls, line_item_id):
        db_response = cls.db.execute_select("meta_key, meta_value", cls.items_details_table, condition=f"order_item_id = {line_item_id}") 
        details = {row['meta_key']:row['meta_value'] for row in db_response}
        logger.debug(details)
        return details
