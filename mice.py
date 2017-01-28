import numpy as np
from test import generate_data
from ml import LinearRegression

def mice(data):
    """Multivariate Imputation by Chained Equations"""
    null_indices = np.argwhere(np.isnan(data))
    null_indices = np.append(null_indices,np.zeros((np.shape(null_indices)[0],1)),axis=1) # Add a column of zeros to the index values
    null_indices = [[int(x),int(y),v] for x,y,v in null_indices]
    temp = []
    cols_missing = set([y  for _,y,__ in null_indices])

    # Step 1: Simple Imputation, these are just placeholders
    for x,y,value in null_indices: 
        print("data[{}][{}] = {}/{}".format(x,y,value,data[x][y]))
        col = data[:,[y]][~np.isnan(data[:,[y]])] # Column containing nan value without the nan value
        new_value = np.mean(col)
        data[x][y] = new_value
        temp.append([x,y,new_value])
    null_indices = temp

    for _ in range(100):
        # Step 2: Placeholders are set back to missing for one variable/column
        dependent_col = int(np.floor(np.random.random() * (len(cols_missing)+1)))
        missing_xs = [x for x,y,value in null_indices if y == dependent_col]

        # Step 3: Perform linear regression using the other variables
        X_train,Y_train = [],[]
        for x in (x for x in range(len(data)) if x not in missing_xs):
            X_train.append(np.delete(data[x],dependent_col))
            Y_train.append(data[x][dependent_col])
        model = LinearRegression()
        model.train(X_train,Y_train)
        
        # Step 4: Missing values for the missing variable/column are replaced with predictions from our new linear regression model
        temp = []
        for x,y,value in ([x,y,value]  for x,y,value in null_indices if y == dependent_col): # For null indices with the dependent column that was randomly chosen
            print("data[{}][{}] = {}/{}".format(x,y,value,data[x][y]))
            new_value = model.predict(data[x][~np.isnan(data[x])]) # Row 'x' without the nan value 
            data[x][y] = new_value
            temp.append([x,y,new_value])
        null_indices = temp
    # Step 5: Steps 2-4 Repeated for each variable that has missing data
    # Step 6: Steps 2-4 Repeated are repeated for a number of cycles with the imputations being updated at each cycle. By the end, we should have imputations that have converged

        


data = generate_data()
mice(data)
