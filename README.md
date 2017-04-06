[![travis-CI](https://travis-ci.org/eltonlaw/impy.svg?branch=master)](https://travis-ci.org/eltonlaw/impy)


# impy

This is a library of missing data imputation algorithms written in Python 3. This 

``` python3
>>> from impy.datasets import random_uniform
>>> raw_data = random_uniform(shape=(5, 5), missingness="mcar", th=0.2)
>>> print(raw_data)
[[  1.   0.   4.   0.   1.]
 [  1.  nan   6.   4.  nan]
 [  5.   0.  nan   1.   3.]
 [  2.   1.   5.   4.   6.]
 [  2.   1.   0.   0.   6.]]
>>> from impy.imputations.cs import mean_imputation   
>>> complete_data = random_imputation(raw_data) 
>>> print(complete_data)
[[ 1.    0.    4.    0.    1.  ]
 [ 1.    0.5   6.    4.    4.  ]
 [ 5.    0.    3.75  1.    3.  ]
 [ 2.    1.    5.    4.    6.  ]
 [ 2.    1.    0.    0.    6.  ]]
```

## Install

To install impy, run the following:

``` shell
$ pip install impy
```

## Documentation

Documentation is available here: http://impy.readthedocs.io/

## Contributing

Check out https://github.com/eltonlaw/impy/blob/master/CONTRIBUTING.md
