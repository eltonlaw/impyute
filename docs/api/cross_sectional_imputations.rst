============================
 Cross Sectional Imputation
============================

-------------------
 Random Imputation 
-------------------

Defined in `impyute.imputations.cs.random_imputation <https://github.com/eltonlaw/impyute/blob/master/impyute/imputations/cs/random_imputation.py>`_

.. code-block:: python

    random_imputation(
     data
    )

^^^^^^
 Args
^^^^^^

* `data`: A 2D Matrix. Must be a `numpy.array <https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html>`_ of `dtype` `float32`, `float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`.

--------------------------------------------------------------------------------------------------------

--------------------------
 Expectation Maximization 
--------------------------

Defined in `impyute.imputations.cs.em <https://github.com/eltonlaw/impyute/blob/master/impyute/imputations/cs/em.py>`_

Imputes given data using the expectation maximizaton algorithm.

.. code-block:: python

    em(
     data,
     loops=50,
     dtype="cont"
    )

^^^^^^
 Args
^^^^^^

* `data`: A 2D Matrix. Must be a `numpy.array <https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html>`_ of `dtype` `float32`, `float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`.
* `loops`: Number of EM training iterations to run before breaking (Note that the algorithm will also break out of the loop if the likelihood doesn't change by at least 10% after 5 runs)
* `dtype`: Must be string `cont` or `disc` to indicate whether the imputed data is continuous (`float32, `float64`) or discrete(`int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`)

--------------------------------------------------------------------------------------------------------

----------------------------------------------
 Multivariate Imputation by Chained Equations 
----------------------------------------------

Defined in `impyute.imputations.cs.mice <https://github.com/eltonlaw/impyute/blob/master/impyute/imputations/cs/mice.py>`_

Imputes given data using the "Multivariate Imputation By Chained Equations" method.

.. code-block:: python

    mice(
     data
    )

^^^^^^
 Args
^^^^^^

* `data`: A 2D Matrix. Must be a `numpy.array <https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html>`_ of `dtype` `float32`, `float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`.

--------------------------------------------------------------------------------------------------------

-----------------
 Mean Imputation 
-----------------

Defined in `impyute.imputations.cs.averaging_imputations <https://github.com/eltonlaw/impyute/blob/master/impyute/imputations/cs/averaging_imputations.py>`_

Imputes given data by filling with the mean of the column.

.. code-block:: python

    mean_imputation(
     data
    )

^^^^^^
 Args
^^^^^^

* `data`: A 2D Matrix. Must be a `numpy.array <https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html>`_ of `dtype` `float32`, `float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`.

--------------------------------------------------------------------------------------------------------

-----------------
 Mode Imputation 
-----------------

Defined in `impyute.imputations.cs.averaging_imputations <https://github.com/eltonlaw/impyute/blob/master/impyute/imputations/cs/averaging_imputations.py>`_

Imputes given data by filling with the mode of the column.

.. code-block:: python

    mode_imputation(
     data
    )

^^^^^^
 Args
^^^^^^

* `data`: A 2D Matrix. Must be a `numpy.array <https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html>`_ of `dtype` `float32`, `float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`.

--------------------------------------------------------------------------------------------------------

-------------------
 Median Imputation 
-------------------

Defined in `impyute.imputations.cs.averaging_imputations <https://github.com/eltonlaw/impyute/blob/master/impyute/imputations/cs/averaging_imputations.py>`_

Imputes given data by filling with the median of the column.

.. code-block:: python

    median_imputation(
     data
    )

^^^^^^
 Args
^^^^^^

* `data`: A 2D Matrix. Must be a `numpy.array <https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html>`_ of `dtype` `float32`, `float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`.
