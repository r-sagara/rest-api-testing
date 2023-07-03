import pytest
import logging as logger
from tests.test_data.customer import CustomerTestData
from src.helpers.apis.customer import CustomerHelper
from src.helpers.dao.customer import CustomerDAO
import src.utilities.generic as gen_utils


@pytest.mark.tcid_29
def test_create_customer_with_only_email_and_password():
    logger.info("TEST: Verify 'POST /customers' creates user with email and password only")
    
    email = gen_utils.generate_random_email()
    customer_payload = CustomerTestData.get_customer_payload(email=email, password="TEST")
    customer_response = CustomerHelper.create_new_item(customer_payload)
    
    customer_response_code = customer_response["status_code"]
    assert customer_response_code == 201, f"Response status code is wrong: {customer_response_code}. Expected: {201}"

    customer_json = customer_response['json']
    assert customer_json['email'] == email, f"Emails in request and response are not equal"
    assert customer_json['username'] == email.split('@')[0], f"Username in response is not equal to email name in request"
    assert not customer_json['first_name'], f"First name is not empty value, although it wasn't sent in request"
    
    customer_db_records = CustomerDAO.get_item_by_email(email)
    assert len(customer_db_records) == 1, f"The number of records with such email {email} is not equal to 1"
    assert customer_db_records[0]['ID'] == customer_json['id'], f"User ID in response and database are not equal"


@pytest.mark.tcid_47
def test_create_customer_with_existing_email():
    logger.info("TEST: Verify 'create customer' failes if email exists")

    customer_from_db = CustomerDAO.get_last_item_in_table()
    email = customer_from_db['user_email']

    customer_payload = CustomerTestData.get_customer_payload(email=email)
    customer_response = CustomerHelper.create_new_item(customer_payload)
    
    customer_response_code = customer_response['status_code']
    assert customer_response_code == 400, f"Response status code is wrong: {customer_response_code}. Expected: {400}"
    assert customer_response['json']['code'] == "registration-error-email-exists"