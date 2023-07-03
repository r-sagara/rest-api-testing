class OrderTestData:
    __order_template = {
        "payment_method": "bacs",
        "payment_method_title": "Test Method",
        "set_paid": None,
        "billing": {
            "first_name": "Test Name",
            "last_name": "Test Name",
            "address_1": "969 Market",
            "address_2": "",
            "city": "San Francisco",
            "state": "CA",
            "postcode": "94103",
            "country": "US",
            "email": None,
            "phone": "(555) 555-5555"
        },
        "line_items": []
    }

    @classmethod
    def get_order_payload(cls, paid=True, customer_id=None, email=None, line_items_ids=None, product_qty=1):
        order_copy = cls.__order_template.copy()
        order_copy['set_paid'] = paid
        order_copy['billing']['email'] = email
        if customer_id:
            order_copy['customer_id'] = customer_id
        for line_item_id in line_items_ids:
            order_copy['line_items'].append({"product_id": line_item_id, "quantity": product_qty})
        return order_copy
    