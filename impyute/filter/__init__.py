"""
The :mod: impyute.filter module provides filtering algorithms to be used with
time series imputation using expectation maximization
"""
from .alpha_beta import alpha_beta

__all__ = ["alpha_beta"]
