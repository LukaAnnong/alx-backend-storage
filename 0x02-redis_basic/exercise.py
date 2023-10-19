#!/usr/bin/env python3
"""
Cache module
"""

import sys
import redis
import uuid
from typing import Union, Callable
from functools import wraps
