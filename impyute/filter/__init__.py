"""
The :mod: impyute.filter module provides filtering algorithms to be used with
time series imputation using expectation maximization
"""
from .kalman import Kalman

__all__ = ["Kalman"]
