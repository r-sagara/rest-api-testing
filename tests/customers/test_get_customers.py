import pytest
import logging as logger
from src.helpers.dao.customer import CustomerDAO
from src.helpers.apis.customer import CustomerAPI


@pytest.mark.tcid_30
def test_get_list_of_all_customers():
    logger.info("TEST: Verify 'GET /customers' lists all users")
    
    customers = CustomerAPI.get_items()
    customers_code = customers["status_code"]
    assert customers_code == 200, f"Response status code is wrong: {customers_code}. Expected: {200}"
    
    customers_json = customers["json"]
    assert customers_json, f"Customers list is empty"
    customer_db_records = CustomerDAO.get_all_items()
    assert len(customer_db_records) == len(customers_json), f"Number of users in database ({len(customer_db_records)}) and response ({len(customers_json)}) is not equal"