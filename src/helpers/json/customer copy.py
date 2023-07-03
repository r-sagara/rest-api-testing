import src.utilities.generic as gen_utils
from typing import Dict

class Customer:
    
    def __init__(self, email:str=None, password:str=None) -> None:
        self.email = email if email is not None else gen_utils.generate_random_email()
        self.password = password if password is not None else gen_utils.generate_random_password()

    def payload(self) -> Dict:
        return {
            "email": self.email,
            "password": self.password
        }