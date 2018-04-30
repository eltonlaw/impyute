"""
Real-world/mock datasets and missingness corruptors to experiment with.
"""
from .base import randu
from .base import randn
from .base import test_data
from .base import mnist

__all__ = ["randu", "randn", "test_data", "mnist"]
