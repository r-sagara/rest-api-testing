import pytest
import logging as logger
from src.helpers.dao.product import ProductDAO
from src.helpers.apis.product import ProductAPI


@pytest.fixture(scope='function')
def created_product_id():
    response_create = ProductAPI.create_new_item()
    id = response_create['json']['id']
    logger.debug(f"Product created: {id}")
    yield id
    ProductDAO.delete_item_by_id(id)
    logger.debug(f"Product deleted: {id}")