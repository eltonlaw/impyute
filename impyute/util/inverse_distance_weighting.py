""" impyute.util.inverse_distance_weighting """
import numpy as np

def shepards(distances, power=1):
    return to_percentage(1/np.power(distances, power))

def to_percentage(arr):
    return arr/np.sum(arr)
