from dataclasses import dataclass


@dataclass(frozen=True)
class Templates:
    paid_order = {
        "payment_method": "bacs",
        "payment_method_title": "Test Method",
        "set_paid": True,
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
        "line_items": [
            {
                "product_id": None,
                "quantity": 1
            }
        ]
    }