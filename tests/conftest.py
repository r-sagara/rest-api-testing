import pytest
import logging as logger
from src.helpers.dao.product import ProductDAO
from src.helpers.apis.product import ProductAPI
from tests.test_data.templates import Templates
from src.helpers.apis.order import OrderAPI
from src.utilities.generic import generate_random_email


@pytest.fixture(scope='function')
def created_product_id():
    response_create = ProductAPI.create_new_item()
    id = response_create['json']['id']
    logger.debug(f"Product created: {id}")
    yield id
    ProductDAO.delete_item_by_id(id)
    logger.debug(f"Product deleted: {id}")


@pytest.fixture(scope='function')
def created_order():
    product_price = 120
    response_create = ProductAPI.create_new_item(params={'regular_price': str(product_price)})
    created_product = response_create['json']
    
    payload = Templates.paid_order.copy()
    
    line_item_link = payload['line_items'][0]
    line_item_link['product_id'] = created_product['id']
    line_item_link['quantity'] = 1

    response = OrderAPI.create_new_item(params=payload)
    return response['json']