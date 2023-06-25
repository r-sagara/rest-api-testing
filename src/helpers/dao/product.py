from src.helpers.dao.general import GeneralDAO
import logging as logger

class ProductDAO(GeneralDAO):
    table = "wp_posts"
    details_table = "wp_postmeta"

    @classmethod
    def get_last_item_in_table(cls):
        last_item = cls.db.execute_select("*", cls.table, order_by="id desc", condition="post_type = 'product'")[0]
        logger.debug(last_item)
        return last_item
    
    @classmethod
    def get_product_details_by_id(cls, product_id):
        db_response = cls.db.execute_select("meta_key, meta_value", cls.details_table, condition=f"post_id = {product_id}") 
        details = {row['meta_key']:row['meta_value'] for row in db_response}
        logger.debug(details)
        return details
