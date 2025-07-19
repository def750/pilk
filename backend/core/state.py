from __future__ import annotations
from argon2 import PasswordHasher

from settings import Config

PASSWORD_HASHER = PasswordHasher(
    time_cost=Config.Service.Argon2.time_cost,
    memory_cost=Config.Service.Argon2.memory_cost,
    parallelism=Config.Service.Argon2.parallelism,
    hash_len=Config.Service.Argon2.hash_length,
    salt_len=Config.Service.Argon2.salt_length,
    type=Config.Service.Argon2.type,
)
