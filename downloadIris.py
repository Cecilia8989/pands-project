''' This script will import the iris dataset from the url 
https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data' 
and it convert it to a csv using pandas. Csv is save in the current directory
'''

# Author: Cecilia Pastore 
# downloadiris.py 

# Import pandas library
import pandas as pd 

# Define the URL from which to download the dataset 
csv_ulr =  'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# Set the column names of the dataset to correspond with the attribute information 
col_names = ['SepalLenght(cm)', 'SepalWidth(cm)', 'PetalLenght(cm)', 'PetalWidth(cm)', 'Species']

# download the dataset and change the colums 
iris =  pd.read_csv(csv_ulr, names = col_names)

# Save the dataset as a CSV file 
iris.to_csv("iris_dataset.csv", index=False)
print("iris_dataset.csv created")



