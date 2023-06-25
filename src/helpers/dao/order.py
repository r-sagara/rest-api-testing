from src.helpers.dao.general import GeneralDAO
import logging as logger

class OrderDAO(GeneralDAO):
    table = "wp_woocommerce_order_items"
