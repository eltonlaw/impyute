import numpy as np
# from ml import LinearRegression
from sklearn.linear_model import LinearRegression
from impy.diagnostics import find_null


def MICE(data):
    """Multivariate Imputation by Chained Equations

    PARAMETERS
    ---------
    data: numpy.ndarray

    RETURNS
    ------
    numpy.ndarray
    """
    null_xyv = find_null(data)

    # Add a column of zeros to the index values
    null_xyv = np.append(null_xyv, np.zeros(np.shape(null_xyv)[0], 1), axis=1)

    null_xyv = [[int(x), int(y), v] for x, y, v in null_xyv]
    temp = []
    cols_missing = set([y for _, y, _ in null_xyv])

    # Step 1: Simple Imputation, these are just placeholders
    for x_i, y_i, value in null_xyv:
        # Column containing nan value without the nan value
        col = data[:, [y_i]][~np.isnan(data[:, [y_i]])]

        new_value = np.mean(col)
        data[x_i][y_i] = new_value
        temp.append([x_i, y_i, new_value])
    null_xyv = temp

    # Step 5: Repeat step 2 - 4 until convergence (the 100 is arbitrary)
    for _ in range(100):
        # Step 2: Placeholders are set back to missing for one variable/column
        dependent_col = int(np.random.choice(list(cols_missing)))
        missing_xs = [int(x) for x, y, value in null_xyv if y == dependent_col]

        # Step 3: Perform linear regression using the other variables
        X_train, Y_train = [], []
        for x_i in (x_i for x_i in range(len(data)) if x_i not in missing_xs):
            X_train.append(np.delete(data[x_i], dependent_col))
            Y_train.append(data[x_i][dependent_col])
        model = LinearRegression()
        model.fit(X_train, Y_train)

        # Step 4: Missing values for the missing variable/column are replaced
        # with predictions from our new linear regression model
        temp = []
        # For null indices with the dependent column that was randomly chosen
        for x_i, y_i, value in ([x_i, y_i, value]
                                for x_i, y_i, value in null_xyv
                                if y_i == dependent_col):
            # Row 'x' without the nan value
            new_value = model.predict(np.delete(data[x_i], dependent_col))

            data[x_i][y_i] = new_value.reshape(1, -1)
            temp.append([x_i, y_i, new_value])
        null_xyv = temp
    return data
