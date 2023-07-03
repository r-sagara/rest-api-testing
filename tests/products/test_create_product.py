import pytest
import logging as logger
from src.helpers.apis.product import ProductHelper
from src.helpers.dao.product import ProductDAO


@pytest.mark.tcid_26
def test_create_simple_product():
    logger.info("TEST: Verify 'POST /products' creates a simple product")
    
    product_response = ProductHelper.create_new_item()
    expected_product_object = {
        'name': "Product",
        'type': "simple"
    }
    
    response_code = product_response['status_code']
    assert response_code == 201, f"Response status code is wrong: {response_code}. Expected: {201}"

    product_json = product_response['json']
    for key in expected_product_object:
        assert product_json[key] == expected_product_object[key], f"Product '{key}' is not default. Given: {product_json[key]}. Expected: {expected_product_object[key]}"

    product_id = product_json['id']
    db_product = ProductDAO.get_item_by_id(id=product_id)
    assert db_product['post_title'] == expected_product_object['name']