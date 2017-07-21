.. image:: https://travis-ci.org/eltonlaw/impyute.svg?branch=master
    :target: https://travis-ci.org/eltonlaw/impyute

.. image:: https://img.shields.io/pypi/v/impyute.svg
    :target: https://pypi.python.org/pypi/impyute

Impyute
========

Impyute is a library of missing data imputation algorithms written in Python 3. This library was designed to be super lightweight, here's a sneak peak at what impyute can do. 

.. code-block:: python

    >>> from impyute.datasets import random_uniform
    >>> raw_data = random_uniform(shape=(5, 5), missingness="mcar", th=0.2)
    >>> print(raw_data)
    [[  1.   0.   4.   0.   1.]
     [  1.  nan   6.   4.  nan]
     [  5.   0.  nan   1.   3.]
     [  2.   1.   5.   4.   6.]
     [  2.   1.   0.   0.   6.]]
    >>> from impyute.imputations.cs import mean_imputation   
    >>> complete_data = random_imputation(raw_data) 
    >>> print(complete_data)
    [[ 1.    0.    4.    0.    1.  ]
     [ 1.    0.5   6.    4.    4.  ]
     [ 5.    0.    3.75  1.    3.  ]
     [ 2.    1.    5.    4.    6.  ]
     [ 2.    1.    0.    0.    6.  ]]

Feature Support
---------------

* Imputation of Cross Sectional Data
    * Multivariate Imputation by Chained Equations
    * Expectation Maximization
    * Mean Imputation
    * Mode Imputation
    * Median Imputation
    * Random Imputation
* Imputation of Time Series Data
    * Last Observation Carried Forward
    * Autoregressive Integrated Moving Average (WIP)
    * Expectation Maximization with the Kalman Filter (WIP)
* Dataset Generation
    * Datasets
        * MNIST
        * Random uniform distribution
        * Random gaussian distribution
    * Missingness Corruptors
        * MCAR
        * MAR (WIP)
        * MNAR (WIP)
* Diagnostic Tools
    * Loggers
    * Distribution of Null Values
    * Comparison of imputations
    * Little's MCAR Test (WIP)

Installation
------------

To install impyute, run the following:

.. code-block:: bash

    $ pip install impyute

Or to get the most current version:

.. code-block:: bash
    
    $ git clone https://github.com/eltonlaw/impyute
    $ cd impyute
    $ python setup.py install

Documentation
-------------

Documentation is available here: http://impyute.readthedocs.io/


How to Contribute
-----------------

Check out CONTRIBUTING_

.. _CONTRIBUTING: https://github.com/eltonlaw/impyute/blob/master/CONTRIBUTING.md

