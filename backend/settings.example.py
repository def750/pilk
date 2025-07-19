### I'm too fucking lazy to implement yaml reader and I hate .env files so here's this shit
### I do not care that I should follow industry standards, It's my repository and I do what I want

from dataclasses import dataclass


@dataclass
class Config:
    class General:
        name = "Pilk"
        version = "1.0.0"
        author = "changeme"
        description = "Account and service management for sillynet"
        domain = "changeme"
        debug = True

    class Database:
        class Postgres:
            host = "changeme"
            port = 5432
            username = "changeme"
            password = "changeme"
            database = "changeme"

        class Redis:
            host = "changeme"
            port = 6379
            password = "changeme"
            db = 0

    class Logging:
        level = "INFO"
        file = "app.log"
        max_size = 10 * 1024 ^ 2  # 10 MB
        max_backups = 5
        max_age = 30
        compress = True

    class Service:
        class Backend:
            host = "changeme"
            port = 8001
            cors_allow_origins = ["changeme"]
            secret_key = "changeme"

        class Argon2:
            time_cost = 2
            memory_cost = 65536
            parallelism = 2
            hash_length = 32
            salt_length = 16
            type = "argon2id"

        class Frontend:
            host = "changeme"
            port = 8002
            static_dir = "static"

    class Security:
        csrf_protection = True
        session_timeout = "15m"

        class PasswordPolicy:
            min_length = 8
            require_uppercase = True
            require_lowercase = True
            require_numbers = True
            require_special = True
