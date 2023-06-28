HOSTS = {
    "machine1": {
        "test": {
            "api": {
                "host": "http://192.168.56.1:8080/wowsite/wp-json/wc/v3"
            },
            "db": {
                "host": "localhost",
                "socket": None,
                "port": 3306,
                "name": "wowsite"
            }
        },
        "dev": None,
        "prod": None
    },
    "docker": {
        "test": {
            "api": {
                "host": "http://192.168.56.1:8080/wowsite/wp-json/wc/v3"
            },
            "db": {
                "host": "host.docker.internal",
                "socket": None,
                "port": 3306,
                "name": "wowsite"
            }        
        },
        "dev": None,
        "prod": None
    }
}