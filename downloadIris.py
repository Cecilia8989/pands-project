import pandas as pd 

# Download the iris data set 
csv_ulr =  'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# using the attribute inforamtion as the column names 
col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']
iris =  pd.read_csv(csv_ulr, names = col_names)

# save the dataset as CSV FILE 
iris.to_csv("iris_dataset.csv", index=False)



