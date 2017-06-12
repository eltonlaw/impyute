===========
 Utilities
===========

`impyute.utils <https://github.com/eltonlaw/impyute/blob/master/impyute/utils>`_

---------
 Compare 
---------

Compare the classification accuracy of multiple algorithms on passed datasets(imputed). Currently uses the following four classification algorithms: `SVC <http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC>`_, `KNeighbours <http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier>`_, `GaussianNB <http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html>`_ and `RandomForestClassifier <http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html>`_

Defined in `impyute.utils.compare <https://github.com/eltonlaw/impyute/blob/master/impyute/utils/compare.py>`_

.. code-block:: python

    compare(
      imputed,
      log_path="results.txt"
    )

^^^^^^
 Args
^^^^^^

* `data`: A 3D Matrix. Elements can only be a complete(no NaN values) `numpy.array <https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html>`_ of `dtype` `float32`, `float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`.
* `log_path`: Path that classification results are written to. Must be a valid string usable by the `.write` method of a python `file object <https://docs.python.org/3.6/tutorial/inputoutput.html>`_ 

---------------
 Count Missing 
---------------

Counts the total percentage of missing values and total percentage attributable to each column. Returns a dictionary with keys `total`, `0`, `1`, ... `n` with n columns. Missing values are anything considered `True` by `numpy.isnan <https://docs.scipy.org/doc/numpy/reference/generated/numpy.isnan.html>`_

Defined in `impyute.utils.find_null <https://github.com/eltonlaw/impyute/blob/master/impyute/utils/find_null.py>`_

.. code-block:: python

    count_missing(
     data
    )

^^^^^^
 Args
^^^^^^

* `data`: A 2D Matrix. Must be a `numpy.array <https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html>`_ of `dtype` `float32`, `float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`.

-----------
 Find Null 
-----------

Finds the indices of all missing values. Missing values are anything considered `True` by `numpy.isnan <https://docs.scipy.org/doc/numpy/reference/generated/numpy.isnan.html>`_

Defined in `impyute.utils.find_null <https://github.com/eltonlaw/impyute/blob/master/impyute/utils/find_null.py>`_

.. code-block:: python

    find_null(
     data
    )

^^^^^^
 Args
^^^^^^

* `data`: A 2D Matrix. Must be a `numpy.array <https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html>`_ of `dtype` `float32`, `float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`.
