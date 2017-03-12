[![travis-CI](https://travis-ci.org/eltonlaw/impy.svg?branch=master)](https://travis-ci.org/eltonlaw/impy)

# Imputations

This is a library of missing data imputation algorithms written in Python 3.

Data can be missing from a dataset for various reasons. Dependent upon the specific reason a cell is missing, we will have to treat each missing value differently:

- Missing Completely At Random (MCAR): Data is missing independent of both observed
  and unobserved variables
- Missing at Random (MAR): Data is missing independent of unobserved data, but
  dependent of observed data
- Missing Not At Random (MNAR): Data is missing due to the values of those missing
  values. 

## Install

``` shell
$ git clone https://github.com/eltonlaw/impy.git
$ cd impy 
$ pip install -e .
```
  
## Quick Demonstration

``` shell
$ python3
```

``` python3
>>> from impy.datasets import random_int
>>> data_w_missing = random_int()
>>> print(raw_data)
[[  1.   0.   4.   0.   1.]
 [  1.  nan   6.   4.  nan]
 [  5.   0.  nan   1.   3.]
 [  2.   1.   5.   4.   6.]
 [  2.   1.   0.   0.   6.]]
>>> from impy.basic import random_imputation     
>>> data_filled = random_imputation(data_w_missing) 
>>> print(data_filled)
[[ 1.    0.    4.    0.    1.  ]
 [ 1.    0.5   6.    4.    4.  ]
 [ 5.    0.    3.75  1.    3.  ]
 [ 2.    1.    5.    4.    6.  ]
 [ 2.    1.    0.    0.    6.  ]]
```

## Imputations

**Random Imputation:** Fill in missing values with a randomly selected value from the same column. Not very useful, but acts as a good baseline.

**Mean Imputation:** The missing value is replaced by the mean of the available data in that column. 

**Mode Imputation:** The missing value is replaced by the mode of the available data in that column. 

**Median Imputation:** The missing value is replaced by the median of the available data in that column. 

**Multivariate Imputation by Chained Equations:** Underlying assumption that data is MAR. First perform simple imputation for each missing value, then for one category/column set the filled values in it back to missing. Train a linear regression model, setting the dependent variable as the column you just chose. Using the trained model, predict the missing variables. Repeat until values converge for all columns with missing variables.

**Expectation Maximization:** An iterative method to estimate missing data values by splitting up the imputaton process into two parts. Model/parameter estimation is done then used to predict new values. These new values in turn are used to calculate error and model/parameter values are retuned then actual values are predicted again. This happens over and over until it converges.

**Last Observation Carried Forward:** For each missing value substitute the preceding value. If the missing value is in the first column, substitute the next value instead. For time series data only. 

## Deletion Methods

**Complete Case:** Only use datapoints with complete data aka drops all rows with missing data. May waste alot of data.



## Citations

Schmitt P, Mandel J, Guedj M (2015) A Comparison of Six Methods for Missing Data Imputation. J Biom Biostat 6:224. doi: 10.4172/2155-6180.1000224

Gelman A, Hill J (2006) Data Analysis Using Regression and Multilevel/Hierarchical Models.  

Azur MJ, Stuart EA, Frangakis C, Leaf PJ. Multiple Imputation by Chained Equations:
What is it and how does it work? International journal of methods in psychiatric
research. 2011;20(1):40-49. doi:10.1002/mpr.329.

