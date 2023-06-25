import logging as logger
import random
from string import ascii_lowercase, ascii_letters, digits, punctuation


def generate_random_email(domain:str='wowsite.com', random_len:int=10, email_prefix:str='testuser_'):
    logger.debug("Generating random email")
    charset = ascii_lowercase + digits
    email = email_prefix + ''.join(random.choices(charset, k=random_len))
    return f"{email}@{domain}"
    
def generate_random_password(length:int=8):
    logger.debug("Generating random password")
    charset = ascii_letters + digits + punctuation
    return ''.join(random.choices(charset, k=length))
