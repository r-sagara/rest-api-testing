import pytest
import logging as logger
from src.helpers.dao.product import ProductDAO
from src.helpers.apis.product import ProductHelper
from tests.test_data.order import OrderTestData
from src.helpers.apis.order import OrderHelper


@pytest.fixture(scope='function')
def created_product_id():
    response_create = ProductHelper.create_new_item()
    id = response_create['json']['id']
    logger.debug(f"Product created: {id}")
    yield id
    ProductDAO.delete_item_by_id(id)
    logger.debug(f"Product deleted: {id}")


@pytest.fixture(scope='function')
def created_order():
    product_price = 120
    response_create = ProductHelper.create_new_item(params={'regular_price': str(product_price)})
    created_product = response_create['json']
    
    order_payload = OrderTestData.get_order_payload(line_items_ids=[created_product['id']], 
                                                    product_qty=1)

    response = OrderHelper.create_new_item(params=order_payload)
    return response['json']