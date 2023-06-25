import pytest
import logging as logger
from src.helpers.apis.product import ProductAPI
from src.helpers.dao.product import ProductDAO


@pytest.mark.tcid_61
def test_update_product_regular_price():
    logger.info("TEST: Verify update 'regular_price' updates 'price' field")
    
    response_create = ProductAPI.create_new_item()
    created_product_id = response_create['json']['id']

    new_price = "120.0"
    response_update = ProductAPI.update_item_by_id(created_product_id, params={'regular_price': new_price})
    regular_price_updated = response_update['json']['regular_price']
    price_updated = response_update['json']['price']
    assert regular_price_updated == new_price, f"'regular_price' value of product is not updated. Actual: {regular_price_updated}. Expected: {new_price}"
    assert price_updated == new_price, f"'price' value of product is not equal to updated 'regular_price'. Actual: {price_updated}. Expected: {new_price}"

@pytest.mark.tcid_65
@pytest.mark.tcid_63
def test_update_product_sale_price_more_than_0():
    logger.info("TEST: Verify update 'sale_price > 0' will set field 'on_sale'=True")
    logger.info("TEST: Verify update 'sale_price' updates the 'sale_price' field")
    
    new_price = "120.0"
    response_create = ProductAPI.create_new_item(params={'regular_price': new_price})
    created_product_id = response_create['json']['id']

    sale_price = "80.0" 
    response_update = ProductAPI.update_item_by_id(created_product_id, params={'sale_price': sale_price})

    regular_price_updated = response_update['json']['regular_price']
    price_updated = response_update['json']['price']
    sale_price_updated = response_update['json']['sale_price']
    on_sale_updated = response_update['json']['on_sale']

    assert sale_price_updated == sale_price, f"'sale_price' value of product is not updated. Actual: {sale_price_updated}. Expected: {sale_price}"
    assert regular_price_updated == new_price, f"'regular_price' value of product is changed. Actual: {regular_price_updated}. Expected: {new_price}"
    assert price_updated == sale_price, f"'price' value of product is not updated. Actual: {price_updated}. Expected: {sale_price}"
    assert on_sale_updated, f"'on_sale' value of product is {on_sale_updated}. Expected: {True}"


@pytest.mark.tcid_64
def test_update_product_sale_price_with_empty_value():
    logger.info("TEST: Verify update 'sale_price=" "' will set field 'on_sale'=False")
    
    new_price = "120.0"
    sale_price = "80.0"
    response_create = ProductAPI.create_new_item(params={'regular_price': new_price, 'sale_price': sale_price})
    created_product_id = response_create['json']['id']
    
    response_update = ProductAPI.update_item_by_id(created_product_id, params={'sale_price': " "})

    price_updated = response_update['json']['price']
    sale_price_updated = response_update['json']['sale_price']
    on_sale_updated = response_update['json']['on_sale']

    assert not sale_price_updated, f"'sale_price' value of product is not removed. Actual: {sale_price_updated}"
    assert price_updated == new_price, f"'price' value of product is not changed back. Actual: {price_updated}. Expected: {new_price}"
    assert not on_sale_updated, f"'on_sale' value of product is {on_sale_updated}. Expected: {False}"