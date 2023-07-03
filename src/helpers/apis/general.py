from src.utilities.requests import Request


class BaseHelper:
    endpoint = None

    @classmethod
    def create_new_item(cls, params=None):
        response = Request.post(cls.endpoint, params=params)
        
        return {
            "status_code": response.status_code,
            "json": response.json()
        }

    @classmethod
    def get_items(cls, all=True, custom_params=None):
        params = {
            "page": 1,
            "per_page": 50,
            "role": "all"
        }

        if custom_params:
            params.update(custom_params)

        response = Request.get(cls.endpoint, params=params)
        total_list_of_items = items_per_page = response.json()
        while all and len(items_per_page) == params["per_page"]:
            params["page"] += 1
            response = Request.get(cls.endpoint, params=params)
            items_per_page = response.json()
            total_list_of_items += items_per_page

        return {
            "status_code": response.status_code,
            "json": total_list_of_items
        }
    
    @classmethod
    def get_item_by_id(cls, id):
        response = Request.get(f"{cls.endpoint}/{id}")

        return {
            "status_code": response.status_code,
            "json": response.json()
        }
    
    @classmethod
    def update_item_by_id(cls, id, params=None):
        response = Request.put(f"{cls.endpoint}/{id}", params=params)

        return {
            "status_code": response.status_code,
            "json": response.json()
        }