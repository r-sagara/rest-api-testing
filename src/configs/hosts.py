API_HOSTS = {
    "test": "http://host.docker.internal:8080/wowsite/wp-json/wc/v3",
    # TODO change back to 'localhost' and change approach of using hosts, gather all hosts together
    # DB_HOSTS to HOSTS
    # HOSTS['machine1']['test'] = {'api_host', 'db_host', 'api_port', 'db_port', 'db_name'}
    # OR
    # HOSTS['machine1']['test']['db'] = {'host', 'port', 'name'}
    # HOSTS['machine1']['test']['api'] = {'host'}
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
    "docker": {
        "test": {
            "host": "host.docker.internal",
            "socket": None,
            "port": 3306,
            "name": "wowsite"
        },
        "dev": None,
        "prod": None
    }
}