import numpy as np
import pandas as pd
from impyute.dataset.corrupt import Corruptor
import statsmodels.api as sm

def test_corrupt():
    # Generate data
    mu = [0.0, 2.5]
    stds = [0.05, 0.1]
    corr = 0.8  # correlation
    covs = [[stds[0] ** 2, stds[0] * stds[1] * corr],
            [stds[0] * stds[1] * corr, stds[1] ** 2]]
    X, Y = np.random.multivariate_normal(mu, covs, 1000).T
    data = np.asarray((X, Y)).T

    # Create data with MAR
    amput = Corruptor(data)
    corrupt_data = amput.mar()

    # Check for correctness by comparing fully observed & data with MAR

    # fit OLS on fully observed data
    X = np.array(X).reshape((-1, 1))
    Y = np.array(Y)
    X = sm.add_constant(X)
    full_model = sm.OLS(Y, X).fit()

    # Fit a linear regression
    complete_data_mar = corrupt_data[~np.isnan(corrupt_data).any(axis=1)]
    x = np.array(complete_data_mar[:, 0]).reshape((-1, 1))
    y = np.array(complete_data_mar[:, 1])
    x = sm.add_constant(x)
    model = sm.OLS(y, x).fit()

    # Use model to get predictions for where data is missing
    corrupt_data = pd.DataFrame(corrupt_data)
    index = corrupt_data.loc[pd.isna(corrupt_data[1]), :].index
    x_pred = np.array(corrupt_data.loc[index, 0]).reshape((-1, 1))
    x_pred = sm.add_constant(x_pred)
    y_pred = model.predict(x_pred)

    # refit OLS to compare coefficient
    xx = np.concatenate((x, x_pred))
    yy = np.concatenate((y, y_pred))
    imp_model = sm.OLS(yy, xx).fit()

    # Check for unbiasedness in y_pred
    full_model_coef = [full_model.params[1]-full_model.bse[1], full_model.params[1]+full_model.bse[1]]
    imp_model_coef = imp_model.params[1]

    assert full_model_coef[0] <= imp_model_coef <= full_model_coef[1], "MAR coefficient not within true values"
