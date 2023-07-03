from src.helpers.apis.general import BaseHelper


class OrderHelper(BaseHelper):
    endpoint = "/orders"

    @staticmethod
    def verify_order_json(order_json, expected_customer_id, expected_user_email, expected_product_id, expected_subtotal):
        assert order_json, f"Created order is empty value"
        actual_customer_id = order_json['customer_id']
        actual_user_email = order_json['billing']['email']
        
        created_line_item = order_json['line_items'][0]
        assert created_line_item, f"No line items in created order"
        actual_product_id = created_line_item['product_id']
        actual_subtotal = created_line_item['subtotal']

        assert actual_customer_id == expected_customer_id, f"Customer id in response ({actual_customer_id}) is not equal to specified in request ({expected_customer_id})"
        assert actual_user_email == expected_user_email, f"Guest email in created order ({actual_user_email}) is not equal to specified in request ({expected_user_email})"
        assert actual_product_id == expected_product_id, f"Product id in response ({actual_product_id}) is not equal to specified in request ({expected_product_id})"
        assert float(actual_subtotal) == expected_subtotal, f"Order total amount from response ({actual_subtotal}) is not equal to calculated ({expected_subtotal})"