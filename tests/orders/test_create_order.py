import pytest
import logging as logger
from src.helpers.apis.order import OrderHelper
from src.helpers.dao.order import OrderDAO
from src.helpers.apis.product import ProductHelper
from tests.test_data.order import OrderTestData
from src.helpers.apis.customer import CustomerHelper
from tests.test_data.customer import CustomerTestData
from src.utilities.generic import generate_random_email


@pytest.mark.tcid_48
def test_create_order_as_guest_user():
    logger.info("TEST: Create a 'paid' order with 'guest' customer")

    product_price = 120
    response_create = ProductHelper.create_new_item(params={'regular_price': str(product_price)})
    created_product_id = response_create['json']['id']

    test_user_email = generate_random_email()
    products_qty = 2
    order_payload = OrderTestData.get_order_payload(paid=True,
                                                    email=test_user_email,
                                                    line_items_ids=[created_product_id],
                                                    product_qty=products_qty)
    
    response = OrderHelper.create_new_item(params=order_payload)
    created_order_json = response['json']

    OrderHelper.verify_order_json(created_order_json,
                                  expected_customer_id=0,
                                  expected_user_email=test_user_email,
                                  expected_product_id=created_product_id,
                                  expected_subtotal=products_qty*product_price)
    
    OrderDAO.verify_line_items_by_order_id(created_order_json['id'],
                                           line_items_qty=1,
                                           expected_product_id=created_product_id,
                                           expected_subtotal=products_qty*product_price)
    

@pytest.mark.tcid_49
def test_create_order_with_existing_user():
    logger.info("TEST: Create a 'paid' order with 'new created' customer")

    customer_payload = CustomerTestData.get_customer_payload()
    customer_id = CustomerHelper.create_new_item(params=customer_payload)['json']['id']

    product_price = 120
    response_create = ProductHelper.create_new_item(params={'regular_price': str(product_price)})
    created_product_id = response_create['json']['id']

    products_qty = 2
    order_payload = OrderTestData.get_order_payload(paid=True,
                                                    email=customer_payload['email'],
                                                    customer_id=customer_id,
                                                    line_items_ids=[created_product_id],
                                                    product_qty=products_qty)
    
    response = OrderHelper.create_new_item(params=order_payload)
    created_order_json = response['json']

    OrderHelper.verify_order_json(created_order_json,
                                  expected_customer_id=customer_id,
                                  expected_user_email=customer_payload['email'],
                                  expected_product_id=created_product_id,
                                  expected_subtotal=products_qty*product_price)
    
    OrderDAO.verify_line_items_by_order_id(created_order_json['id'],
                                           line_items_qty=1,
                                           expected_product_id=created_product_id,
                                           expected_subtotal=products_qty*product_price)