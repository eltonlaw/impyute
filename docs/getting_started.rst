=================
 Getting Started
=================

Installation
============

Install via pip::

    $ pip install impyute 

Dependencies
------------

- NumPy
- Pandas
- SciPy
- scikit-learn

Tutorial
========

A simple example of what this library can do::

    >>> from impyute.datasets.random_uniform
    >>> raw_data = random_uniform(shape=(5,5), missingness="mcar")
    >>> print(raw_data)
    >>> [[  1.   0.   4.   0.   1.]
         [  1.  nan   6.   4.  nan]
         [  5.   0.  nan   1.   3.]
         [  2.   1.   5.   4.   6.]
         [  2.   1.   0.   0.   6.]]
    >>> from impyute.imputations.cs import mean_imputation
    >>> complete_data = mean_imputation(raw_data)
    >>> print(complete_data)
        [[ 1.    0.    4.    0.    1.   ]
         [ 1.    0.5   6.    4.    4.   ]
         [ 5.    0.    3.75  1.    3.   ]
         [ 2.    1.    5.    4.    6.   ]
         [ 2.    1.    0.    0.    6.   ]]

Basically, this generates a dataset complete with missing values which then gets passed as a parameter to one of the available imputation functions a filled dataset is returned.
