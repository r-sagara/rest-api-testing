import pytest
import logging as logger
from src.helpers.apis.product import ProductHelper
from src.helpers.dao.product import ProductDAO


@pytest.mark.tcid_24
def test_get_products_not_empty():
    logger.info("TEST: Verify 'GET /products' does not return empty")
    
    response = ProductHelper.get_items(all=False)
    response_code = response["status_code"]
    assert response_code == 200, f"Response status code is wrong: {response_code}. Expected: {200}"
    
    products_json = response["json"]
    assert products_json, f"Products list is empty"


@pytest.mark.tcid_25
def test_get_product_by_id():
    logger.info("TEST: Verify 'products/id' returns a product with the given id")

    db_product = ProductDAO.get_last_item_in_table()
    db_product_id = db_product['ID']

    response = ProductHelper.get_item_by_id(db_product_id)
    response_code = response['status_code']
    product_json = response['json']
    assert response_code == 200, f"Response status code is wrong: {response_code}. Expected: {200}"
    assert product_json['id'] == db_product_id, f"IDs of product from response ({product_json['id']}) and database ({db_product_id}) are not equal."
    assert product_json['name'] == db_product['post_title'], f"Names of product from response ({product_json['name']}) and database ({db_product['post_title']}) are not equal."
    assert 'price' in product_json, f"There is no 'price' key in returned product JSON: {product_json.keys()}"


@pytest.mark.tcid_51
def test_get_list_of_products_with_after_filter():
    logger.info("TEST: Verify 'List Products' with filter 'after'")

    from datetime import datetime
    timestamp = datetime.utcnow().isoformat()

    created_ids = []
    for count in range(2):
        created_ids.append(ProductHelper.create_new_item()['json']['id'])
    created_ids.sort()

    response = ProductHelper.get_items(all=True, custom_params={"after": timestamp})
    response_code = response['status_code']
    products_json = response['json']

    assert response_code == 200, f"Response status code is wrong: {response_code}. Expected: {200}"
    assert len(products_json) == 2, f"Number of created products after {timestamp} is wrong. Actual: {len(products_json)}. Expected: {len(created_ids)}"

    listed_ids = [item['id'] for item in products_json]
    listed_ids.sort()
    assert created_ids == listed_ids, f"IDs of listed products {listed_ids} are not equal to created ones {created_ids}."