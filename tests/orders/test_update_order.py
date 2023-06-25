import pytest
import logging as logger
from src.helpers.apis.order import OrderAPI
from src.helpers.dao.order import OrderDAO
from src.helpers.apis.product import ProductAPI
from tests.test_data.templates import Templates
from src.utilities.generic import generate_random_email


@pytest.mark.tcid_55
def test_update_order_status():
    logger.info("TEST: Update order status to 'canceled'")

    product_price = 120
    response_create = ProductAPI.create_new_item(params={'regular_price': str(product_price)})
    created_product = response_create['json']

    payload = Templates.paid_order.copy()
    test_user_email = generate_random_email()
    payload['billing']['email'] = test_user_email
    
    line_item_link = payload['line_items'][0]
    line_item_link['product_id'] = created_product['id']
    line_item_link['quantity'] = 2
    
    # response verify
    response = OrderAPI.create_new_item(params=payload)

    created_order = response['json']
    created_line_item = created_order['line_items'][0]
    assert created_order, f"Created order is empty value"
    assert created_line_item, f"No line items in created order"

    assert created_order['billing']['email'] == test_user_email, f"Guest email in created order ({created_order['billing']['email']}) is not equal to specified in request ({test_user_email})"
    assert created_line_item['product_id'] == created_product['id'], f"Product id in response ({created_line_item['product_id']}) is not equal to specified in request ({created_product['id']})"
    
    expected_total_amount = line_item_link['quantity'] * product_price
    assert float(created_line_item['subtotal']) == expected_total_amount, f"Order total amount from response ({created_line_item['subtotal']}) is not equal to calculated ({expected_total_amount})"
    
    db_line_items = OrderDAO.get_line_items_by_order_id(created_order['id'])
    assert len(db_line_items) == len(payload['line_items']), f"Amount of line items in db ({len(db_line_items)}) is not equal to expected {len(payload['line_items'])}"

    # db verify
    db_line_item_details = OrderDAO.get_line_item_details_by_item_id(db_line_items[0]['order_item_id'])
    assert int(db_line_item_details['_line_total']) == expected_total_amount, f"Order total amount from db ({db_line_item_details['_line_total']}) is not equal to calculated ({expected_total_amount})"
    assert int(db_line_item_details['_product_id']) == created_product['id'], f"Order total amount from db ({db_line_item_details['_product_id']}) is not equal to calculated ({created_product['id']})"

