import numpy as np
from test import generate_data
#from ml import LinearRegression
from sklearn.linear_model import LinearRegression

def mice(data):
    """Multivariate Imputation by Chained Equations

    PARAMETERS
    ---------
    data: numpy.ndarray

    RETURNS
    ------
    numpy.ndarray
    
    """
    null_xyv = np.argwhere(np.isnan(data))
    null_xyv = np.append(null_xyv,np.zeros((np.shape(null_xyv)[0],1)),axis=1) # Add a column of zeros to the index values
    null_xyv = [[int(x),int(y),v] for x,y,v in null_xyv]
    temp = []
    cols_missing = set([y  for _,y,__ in null_xyv])

    # Step 1: Simple Imputation, these are just placeholders
    for x,y,value in null_xyv: 
        print("data[{}][{}] = {}/{}".format(x,y,value,data[x][y]))
        col = data[:,[y]][~np.isnan(data[:,[y]])] # Column containing nan value without the nan value
        new_value = np.mean(col)
        data[x][y] = new_value
        temp.append([x,y,new_value])
    null_xyv = temp

    # Step 5: Repeat step 2 - 4 until convergence (the 100 is arbitrary)
    for _ in range(100):
        # Step 2: Placeholders are set back to missing for one variable/column
        dependent_col = int(np.random.choice(list(cols_missing)))
        missing_xs = [int(x) for x,y,value in null_xyv if y == dependent_col]

        # Step 3: Perform linear regression using the other variables
        X_train,Y_train = [],[]
        for x in (x for x in range(len(data)) if x not in missing_xs):
            X_train.append(np.delete(data[x],dependent_col))
            Y_train.append(data[x][dependent_col])
        model = LinearRegression()
        model.fit(X_train,Y_train)
        
        # Step 4: Missing values for the missing variable/column are replaced with predictions from our new linear regression model
        temp = []
        for x,y,value in ([x,y,value]  for x,y,value in null_xyv if y == dependent_col): # For null indices with the dependent column that was randomly chosen
            print("data[{}][{}] = {}/{}".format(x,y,value,data[x][y]))
            new_value = model.predict(np.delete(data[x],dependent_col)) # Row 'x' without the nan value 
            data[x][y] = new_value.reshape(1,-1)
            temp.append([x,y,new_value])
        null_xyv = temp
    return data
