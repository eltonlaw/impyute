"""Configuration Object"""
import numpy as np


def config(data):
    """Hidden Layer Configuraton Object for an Autoencoder

    If a dataset is passed, an architecture is generated.

    PARAMETERS
    ----------
    data: np.ndarray
        A dataset in matrix form

    RETURNS
    -------
    dictionary
    """
    config = {}
    n_data, n_features = np.shape(data)
    config["layers"] = generate_layers(n_data, n_features)
    return config


def generate_layers(n_data, n_features):
    if n_data < 25000:
        n_layers = 2
    elif n_data < 50000:
        n_layers = 3
    elif n_data < 100000:
        n_layers = 4
    layers = []
    for i in range(n_layers):
        rng = ((np.random.random())/2 + 0.5)*(1/(i+2))
        layers.append(rng)
    layers.sort(reverse=True)
    layers[-1] = layers[-1]/3
    layers = np.multiply(layers, n_features)
    layers = layers.astype(np.int)
    return layers
