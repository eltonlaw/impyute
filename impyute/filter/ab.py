"""Implementation of an alpha-beta filter"""
import numpy as np


def ab_filter(data, x_0, dx, alpha, beta, dt=1.):
    """
    data: numpy.nd.array
        Dataset
    x_0: float
        Position of x at time 0
    dx: float
        Change in x
    alpha: [0,1]
        Preference to follow prediction
    beta: [0,1]
        Preference to follow measurement
    dt: float
        Change in time/step-size of time
    """
    x_k = x_0
    positions = []
    for x_mea in data:
        # Prediction
        x_pred = x_k + (dx*dt)
        # Update
        error = x_mea - x_pred
        dx = dx + (beta*error)/dt
        x_k = x_pred + alpha * error
        positions.append(x_k)
    return np.array(positions)
