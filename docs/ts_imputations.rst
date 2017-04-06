=========================
 Time Series Imputations
=========================
------------------
 Time series data
------------------
What is time series data?

*Stationary Data*: Stationary data refers to data with the property that the mean and variance are constant over time. Many time series models assume stationarity as it provides several advantages. 

*Non-stationary Data*: Non-stationarity simply refers to the absence of the stationarity property, there are multiple ways for this to be achieved. 

*Dependence Structure*: Hypothesis about neighbour assumptions



-----------------------------------
 Time Series Imputation Algorithms
-----------------------------------

^^^^^^^
 ARIMA
^^^^^^^
Short for Autoregressive Integrated Moving Average. Autoregressive means that the predicted value incorporates prior values in its calculation.  

# .. autofunction:: imputations.arima
