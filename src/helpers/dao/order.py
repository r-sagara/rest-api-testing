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
    
    @classmethod
    def verify_line_items_by_order_id(cls, order_id, line_items_qty, expected_product_id, expected_subtotal):
        db_line_items = cls.get_line_items_by_order_id(order_id)
        actual_line_items_qty = len(db_line_items)
        assert actual_line_items_qty == line_items_qty, f"Amount of line items in db ({actual_line_items_qty}) is not equal to expected {line_items_qty}"

        db_line_item_details = cls.get_line_item_details_by_item_id(db_line_items[0]['order_item_id'])
        actual_subtotal = int(db_line_item_details['_line_total'])
        actual_product_id = int(db_line_item_details['_product_id'])
        assert actual_subtotal == expected_subtotal, f"Order total amount from db ({actual_subtotal}) is not equal to calculated ({expected_subtotal})"
        assert actual_product_id == expected_product_id, f"Order total amount from db ({actual_product_id}) is not equal to calculated ({expected_product_id})"

