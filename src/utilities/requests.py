from src.configs.hosts import HOSTS
from src.configs.env_setup import APIkeys, Environment
from requests_oauthlib import OAuth1
import logging as logger
import requests
import os
import json


class Request:
    machine = Environment.machine
    assert machine, f"MACHINE variable is empty value"

    env = os.environ.get('ENV', 'test')
    base_url = HOSTS[machine][env]['api']['host']
    oauth = OAuth1(client_key=APIkeys.key, 
                   client_secret=APIkeys.secret)
    
    @classmethod
    def __general_request(cls, method, endpoint, params=None, headers=None, auth=oauth):
        if not headers:
            headers = {"Content-Type": "application/json"}    
        method_interface = getattr(requests, method)
        response = method_interface(url=cls.base_url + endpoint, 
                                    data=json.dumps(params), 
                                    headers=headers,
                                    auth=auth)
        logger.debug(f"Response code: {response.status_code}")
        logger.debug(f"Response JSON: {response.json()}")
        return response
    
    @classmethod
    def post(cls, endpoint, params=None, headers=None):
        return cls.__general_request("post", endpoint, params=params, headers=headers)

    @classmethod
    def get(cls, endpoint, params=None, headers=None):
        return cls.__general_request("get", endpoint, params=params, headers=headers)
    
    @classmethod
    def put(cls, endpoint, params=None, headers=None):
        return cls.__general_request("put", endpoint, params=params, headers=headers)
    
    @classmethod
    def delete(cls, endpoint, params=None, headers=None):
        return cls.__general_request("delete", endpoint, params=params, headers=headers)