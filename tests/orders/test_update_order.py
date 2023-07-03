import pytest
import logging as logger
from src.helpers.apis.order import OrderHelper
from src.helpers.dao.order import OrderDAO


@pytest.mark.parametrize('new_status', [pytest.param("cancelled", marks=pytest.mark.tcid_55),
                                        pytest.param("completed", marks=pytest.mark.tcid_56),
                                        pytest.param("on-hold", marks=pytest.mark.tcid_57)])
def test_update_order_status(created_order, new_status):
    logger.info(f"TEST: Update order status to '{new_status}'")
    
    created_order_id = created_order['id']
    response_update = OrderHelper.update_item_by_id(created_order_id, params={"status": new_status})
    assert response_update['status_code'] == 200, "Wrong status code"

    response = OrderHelper.get_item_by_id(created_order_id)
    updated_status = response['json']['status']
    assert updated_status == new_status, f"Order status is not updated. Actual: {response['status']}. Expected: {new_status}"


@pytest.mark.tcid_58
def test_update_order_status_with_random_string(created_order):
    logger.info("TEST: Update order status to random string")
    
    new_status = 'blabla'
    created_order_id = created_order['id']
    response = OrderHelper.update_item_by_id(created_order_id, params={"status": new_status})
    response_code = response['status_code']
    response_json = response['json']
 
    expected_status_code = 400
    expected_error_code = "rest_invalid_param"
    assert response_code == expected_status_code, f"Received status code ({response_code}) is not equal to expected ({expected_status_code})."
    assert response_json['code'] == expected_error_code, f"Received error code ({response_json['code']}) is not equal to expected ({expected_error_code})."


@pytest.mark.tcid_59
def test_update_order_custom_note(created_order):
    logger.info("TEST: Update order 'customer_note'")
    
    new_customer_note = 'Test customer note'
    created_order_id = created_order['id']
    response_update = OrderHelper.update_item_by_id(created_order_id, params={"customer_note": new_customer_note})
    assert response_update['status_code'] == 200, "Wrong status code"

    response_get = OrderHelper.get_item_by_id(created_order_id)
    assert response_get['status_code'] == 200, "Wrong status code"

    actual_customer_note = response_get['json']['customer_note']
    assert actual_customer_note == new_customer_note, f"Received customer note ({actual_customer_note}) is not equal to expected ({new_customer_note})."
