API_HOSTS = {
    "test": "http://localhost:8080/wowsite/wp-json/wc/v3",
    "dev": "http://localhost:8080/wowsite/wp-json/wc/v3",
    "prod": "http://localhost:8080/wowsite/wp-json/wc/v3"
}

DB_HOSTS = {
    "machine1": {
        "test": {
            "host": "localhost",
            "socket": None,
            "port": 3306,
            "name": "wowsite"
        },
        "dev": None,
        "prod": None
    },
    "work_machine": {
        "test": {
            "host": "localhost",
            "socket": None,
            "port": 3306,
            "name": "wowsite"
        },
        "dev": None,
        "prod": None
    }
}