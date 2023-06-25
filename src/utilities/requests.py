from src.configs.hosts import API_HOSTS
from src.configs.env_setup import APIkeys
from requests_oauthlib import OAuth1
import logging as logger
import requests
import os
import json


class Request:
    env = os.environ.get('ENV', 'test')
    base_url = API_HOSTS[env]
    oauth = OAuth1(client_key=APIkeys.key, 
                   client_secret=APIkeys.secret)
    
    @classmethod
    def __general_request(cls, method, endpoint, payload=None, headers=None, auth=oauth):
        if not headers:
            headers = {"Content-Type": "application/json"}    
        method_interface = getattr(requests, method)
        response = method_interface(url=cls.base_url + endpoint, 
                                    data=json.dumps(payload), 
                                    headers=headers,
                                    auth=auth)
        logger.debug(f"Response code: {response.status_code}")
        logger.debug(f"Response JSON: {response.json()}")
        return response
    
    @classmethod
    def post(cls, endpoint, payload=None, headers=None):
        return cls.__general_request("post", endpoint, payload=payload, headers=headers)

    @classmethod
    def get(cls, endpoint, payload=None, headers=None):
        return cls.__general_request("get", endpoint, payload=payload, headers=headers)
    
    @classmethod
    def put(cls, endpoint, payload=None, headers=None):
        return cls.__general_request("put", endpoint, payload=payload, headers=headers)
    
    @classmethod
    def delete(cls, endpoint, payload=None, headers=None):
        return cls.__general_request("delete", endpoint, payload=payload, headers=headers)