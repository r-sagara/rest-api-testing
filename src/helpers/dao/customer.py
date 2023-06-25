from src.utilities.db_connection import DBConnection
from src.helpers.dao.general import GeneralDAO

class CustomerDAO(GeneralDAO):
    table = "wp_users"

    @classmethod
    def get_item_by_email(cls, email):
        return cls.db.execute_select("*", cls.table, f"user_email = '{email}'")