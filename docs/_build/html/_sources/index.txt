Impyute
========

.. image:: https://travis-ci.org/eltonlaw/impyute.svg?branch=master
    :target: https://travis-ci.org/eltonlaw/impyute

.. image:: https://img.shields.io/pypi/v/impyute.svg
    :target: https://pypi.python.org/pypi/impyute

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
    * Multiple Imputation (WIP)
    * Imputation Using Denoising Stacked Autoencoders (WIP)
* Imputation of Time Series Data
    * Autoregressive Integrated Moving Average (WIP)
    * Expectation Maximization with the Kalman Filter (WIP)
    * Last Observation Carried Forward
* Raw and Complete Dataset Generation
* Tools
    * Loggers
    * Dataset Properties
        * MCAR Test (WIP)
        * Count % of Missing Values
        * Location of Missing Values

Installation
------------

To install impyute, run the following:

.. code-block:: bash

    $ pip3 install impyute


How to Contribute
-----------------

Check out CONTRIBUTING_

.. _CONTRIBUTING: https://github.com/eltonlaw/impyute/blob/master/CONTRIBUTING.md


User Guide
===========

Table of Contents

.. toctree::
   :maxdepth: 2
   
   Getting Started <user_guide/getting_started>
   Overview <user_guide/overview>
   Tutorial <user_guide/tutorial>
   Diagnostics <user_guide/utils>


API
===

.. toctree::
   :maxdepth: 2

   API <api/index>
   GitHub Repo <https://github.com/eltonlaw/impyute>

Contributing
============

.. toctree::
    :maxdepth: 2
    Contributing Guidelines <contributing/index>
    Philosophy <contributing/philosophy>
    Current Goals <contributing/current_goals>

