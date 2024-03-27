#!/usr/bin/env python3
import redis
from typing import Union
from uuid import uuid4


class Cache:
    """Cache Class"""
    def __init__(self) -> None:
        """store an instance of the Redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random key
        Stores the input data in Redis using the key
        Returns the key.
        """
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key
