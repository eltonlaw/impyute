# Imputations

This is a library of missing data imputation algorithms written in Python 3.

Data can be missing from a dataset for various reasons. Dependent upon the specific reason a cell is missing, we will have to treat each missing value differently.

## Basic Methods

**Simple Random Imputation:** Fill in missing values with a randomly selected value from the same column. Not very useful, but acts as a good baseline.
**Complete Case:** Only use datapoints with complete data. May waste alot of data.

## Citations

Schmitt P, Mandel J, Guedj M (2015) A Comparison of Six Methods for Missing Data Imputation. J Biom Biostat 6:224. doi: 10.4172/2155-6180.1000224

Gelman A, Hill J (2006) Data Analysis Using Regression and Multilevel/Hierarchical Models.  

# TODO
* Dataset prediction (randomly take out some values and try to predict them)
* Create a table in the README to compare different algorithms (and on different datasets too)(ex. continuous vs cat vars etc.)

