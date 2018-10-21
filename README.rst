.. image:: https://travis-ci.org/eltonlaw/impyute.svg?branch=master
    :target: https://travis-ci.org/eltonlaw/impyute

.. image:: https://img.shields.io/pypi/v/impyute.svg
    :target: https://pypi.python.org/pypi/impyute

Impyute
========

Impyute is a library of missing data imputation algorithms. This library was designed to be super lightweight, here's a sneak peak at what impyute can do. 

.. code-block:: python

    >>> n = 5
    >>> arr = np.random.uniform(high=6, size=(n, n))
    >>> for _ in range(3):
    >>>    arr[np.random.randint(n), np.random.randint(n)] = np.nan
    >>> print(arr)
    array([[0.25288643, 1.8149261 , 4.79943748, 0.54464834, np.nan],
           [4.44798362, 0.93518716, 3.24430922, 2.50915032, 5.75956805],
           [0.79802036, np.nan, 0.51729349, 5.06533123, 3.70669172],
           [1.30848217, 2.08386584, 2.29894541, np.nan, 3.38661392],
           [2.70989501, 3.13116687, 0.25851597, 4.24064355, 1.99607231]])
    >>> import impyute as impy
    >>> print(impy.mean(arr))
    array([[0.25288643, 1.8149261 , 4.79943748, 0.54464834, 3.7122365],
           [4.44798362, 0.93518716, 3.24430922, 2.50915032, 5.75956805],
           [0.79802036, 1.99128649, 0.51729349, 5.06533123, 3.70669172],
           [1.30848217, 2.08386584, 2.29894541, 3.08994336, 3.38661392],
           [2.70989501, 3.13116687, 0.25851597, 4.24064355, 1.99607231]])

Feature Support
---------------

* Imputation of Cross Sectional Data
    * K-Nearest Neighbours
    * Multivariate Imputation by Chained Equations
    * Expectation Maximization
    * Mean Imputation
    * Mode Imputation
    * Median Imputation
    * Random Imputation
* Imputation of Time Series Data
    * Last Observation Carried Forward
    * Moving Window
    * Autoregressive Integrated Moving Average (WIP)
* Diagnostic Tools
    * Loggers
    * Distribution of Null Values
    * Comparison of imputations
    * Little's MCAR Test (WIP)

Versions
--------

Currently tested on 2.7, 3.4, 3.5, 3.6 and 3.7

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

