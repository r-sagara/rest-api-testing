import pytest
import logging as logger
from src.helpers.apis.order import OrderAPI
from src.helpers.dao.product import ProductDAO
from src.helpers.dao.order import OrderDAO
from src.helpers.apis.product import ProductAPI
from tests.test_data.templates import Templates
from src.utilities.generic import generate_random_email


@pytest.mark.tcid_48
def test_create_order_as_guest_user():
    logger.info("TEST: Create a 'paid' order with 'guest' customer")

    response_create = ProductAPI.create_new_item(params={'regular_price': "120.0"})
    created_product = response_create['json']

    payload = Templates.paid_order.copy()
    test_user_email = generate_random_email()
    payload['billing']['email'] = test_user_email
    line_item_link = payload['line_items'][0]
    line_item_link['product_id'] = created_product['id']
    line_item_link['quantity'] = 2
    
    response = OrderAPI.create_new_item(params=payload)
    import pdb; pdb.set_trace()
    created_order = response['json']
    created_line_item = created_order['line_items'][0]
    assert created_order, f"Created order is empty value"
    assert created_line_item, f"No line items in created order"

    assert created_order['billing']['email'] == test_user_email, f"Guest email in created order ({created_order['billing']['email']}) is not equal to specified in request ({test_user_email})"
    assert created_line_item['product_id'] == created_product['id'], f"Product id in response ({created_line_item['product_id']}) is not equal to specified in request ({created_product['id']})"
    
    expected_total_amount = line_item_link['quantity'] * created_product['price']
    assert created_line_item['subtotal'] == expected_total_amount, f"Order total amount ({created_line_item['subtotal']}) is not equal to calculated ({expected_total_amount})"
    
    db_order_item = OrderDAO.get_item_details_by_id(created_order['id'])

    # get last created product
    # get billing payload for order (create payload generator in heplers? based on name)
    # verify the order is completed

