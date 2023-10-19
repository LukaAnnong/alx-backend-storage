#!/usr/bin/env python3
"""Expiring Web Cache Module"""

import redis
import requests
from typing import Callable
from functools import wraps

# Initialize a Redis client
redis = redis.Redis()

