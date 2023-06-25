import os
from dotenv import find_dotenv, load_dotenv
from dataclasses import dataclass

load_dotenv(find_dotenv())

@dataclass(frozen=True)
class APIkeys:
    key: str = os.environ.get("WC_KEY")
    secret: str = os.environ.get("WC_SECRET")

@dataclass(frozen=True)
class DBkeys:
    user: str = os.environ.get("DB_USER")
    password: str = os.environ.get("DB_PASS")

@dataclass(frozen=True)
class Environment:
    machine: str = os.environ.get('MACHINE')