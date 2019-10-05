import numpy as np
from sklearn.linear_model import LinearRegression
from impyute.ops import matrix
from impyute.ops import wrapper
# pylint: disable=too-many-locals

@wrapper.wrappers
@wrapper.checks
def buck_iterative(data):
    """ Iterative variant of buck's method

    - Variable to regress on is chosen at random.
    - EM type infinite regression loop stops after change in prediction from
      previous prediction < 10% for all columns with missing values

    A Method of Estimation of Missing Values in Multivariate Data Suitable for
    use with an Electronic Computer S. F. Buck Journal of the Royal Statistical
    Society. Series B (Methodological) Vol. 22, No. 2 (1960), pp. 302-306

    Parameters
    ----------
    data: numpy.ndarray
        Data to impute.

    Returns
    -------
    numpy.ndarray
        Imputed data.

    """
    nan_xy = matrix.nan_indices(data)

    # Add a column of zeros to the index values
    nan_xyz = np.append(nan_xy, np.zeros((np.shape(nan_xy)[0], 1)), axis=1)

    nan_xyz = [[int(x), int(y), v] for x, y, v in nan_xyz]
    temp = []
    cols_missing = {y for _, y, _ in nan_xyz}

    # Step 1: Simple Imputation, these are just placeholders
    for x_i, y_i, value in nan_xyz:
        # Column containing nan value without the nan value
        col = data[:, [y_i]][~np.isnan(data[:, [y_i]])]

        new_value = np.mean(col)
        data[x_i][y_i] = new_value
        temp.append([x_i, y_i, new_value])
    nan_xyz = temp

    # Step 5: Repeat step 2 - 4 until convergence (the 100 is arbitrary)

    converged = [False] * len(nan_xyz)
    while not all(converged):
        # Step 2: Placeholders are set back to missing for one variable/column
        dependent_col = int(np.random.choice(list(cols_missing)))
        missing_xs = [int(x) for x, y, value in nan_xyz if y == dependent_col]

        # Step 3: Perform linear regression using the other variables
        x_train, y_train = [], []
        for x_i in (x_i for x_i in range(len(data)) if x_i not in missing_xs):
            x_train.append(np.delete(data[x_i], dependent_col))
            y_train.append(data[x_i][dependent_col])
        model = LinearRegression()
        model.fit(x_train, y_train)

        # Step 4: Missing values for the missing variable/column are replaced
        # with predictions from our new linear regression model
        # For null indices with the dependent column that was randomly chosen
        for i, z in enumerate(nan_xyz):
            x_i = z[0]
            y_i = z[1]
            value = data[x_i, y_i]
            if y_i == dependent_col:
                # Row 'x' without the nan value
                new_value = model.predict([np.delete(data[x_i], dependent_col)])
                data[x_i][y_i] = new_value.reshape(1, -1)
                if value == 0.0:
                    delta = (new_value-value)/0.01
                else:
                    delta = (new_value-value)/value
                converged[i] = abs(delta) < 0.1
    return data
