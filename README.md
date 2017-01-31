# Imputations

This is a library of missing data imputation algorithms written in Python 3.

Data can be missing from a dataset for various reasons. Dependent upon the specific reason a cell is missing, we will have to treat each missing value differently:

- Missing Completely At Random (MCAR): Data is missing independent of both observed
  and unobserved variables
- Missing at Random (MAR): Data is missing independent of unobserved data, but
  dependent of observed data
- Missing Not At Random (MNAR): Data is missing due to the values of those missing
  values. 
  
## Quick Demonstration

``` shell
$ python3
```

``` python3
>>> from test import generate_data
>>> raw_data = generate_data()
>>> print(raw_data)
[[  1.   0.   4.   0.   1.]
 [  1.  nan   6.   4.  nan]
 [  5.   0.  nan   1.   3.]
 [  2.   1.   5.   4.   6.]
 [  2.   1.   0.   0.   6.]]
>>> from basic_imputations import simple_random_imputation     
>>> cleaned_data = simple_random_imputation(raw_data) 
>>> print(cleaned_data)
[[ 1.    0.    4.    0.    1.  ]
 [ 1.    0.5   6.    4.    4.  ]
 [ 5.    0.    3.75  1.    3.  ]
 [ 2.    1.    5.    4.    6.  ]
 [ 2.    1.    0.    0.    6.  ]]
```

## Basic Methods

**Simple Random Imputation:** Fill in missing values with a randomly selected value from the same column. Not very useful, but acts as a good baseline.

**Mean Imputation:** The missing value is replaced by the mean of the available data. 

**Complete Case:** Only use datapoints with complete data. May waste alot of data.

**Last Observation Carried Forward:** For each missing value substitute the preceding value. If the missing value is in the first column, substitute the next value instead. For time series data only. 

## Regression Methods

**Multivariate Imputation by Chained Equations:** Underlying assumption that data is MAR. First perform simple imputation for each missing value, then for one category/column set the filled values in it back to missing. Train a linear regression model, setting the dependent variable as the column you just chose. Using the trained model, predict the missing variables. Repeat until values converge for all columns with missing variables.

## Matching Methods

**Nearest Neighbour Approach:** 

## Citations

Schmitt P, Mandel J, Guedj M (2015) A Comparison of Six Methods for Missing Data Imputation. J Biom Biostat 6:224. doi: 10.4172/2155-6180.1000224

Gelman A, Hill J (2006) Data Analysis Using Regression and Multilevel/Hierarchical Models.  

Azur MJ, Stuart EA, Frangakis C, Leaf PJ. Multiple Imputation by Chained Equations:
What is it and how does it work? International journal of methods in psychiatric
research. 2011;20(1):40-49. doi:10.1002/mpr.329.

## To do
* Create multiple test datasets that each represent the different types of missingness. Compare and contrast which models work best for which types of data, look at variations in standard deviation etc.
* Add hot deck imputation methods
