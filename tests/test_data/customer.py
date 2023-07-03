import src.utilities.generic as gen_utils


class CustomerTestData:

    @classmethod
    def get_customer_payload(cls, email=None, password=None):
        email = email if email is not None else gen_utils.generate_random_email()
        password = password if password is not None else gen_utils.generate_random_password()
        return {
            "email": email,
            "password": password
        }