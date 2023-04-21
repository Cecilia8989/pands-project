
# import needed libraries 
import pandas as pd

# import data from a csv file using pandas 
df = pd.read_csv('iris_dataset.csv')

# change the colums name in a nicer format 
columns = ['Sepal_Lenght(cm)', 'Sepal_Width(cm)', 'Petal_Lenght(cm)', 'Petal_Width(cm)', 'Species']
df.columns = columns

# replace the 3 spieces with a more friendly name 
df["Species"].replace(to_replace="Iris-setosa", value="Setosa", inplace=True)
df["Species"].replace(to_replace="Iris-versicolor", value="Versicolor", inplace=True)
df["Species"].replace(to_replace="Iris-virginica", value="Virginica", inplace=True)
print(df)

# create the tile and write on them 
with open ('iris_analysis.txt', 'w') as f:
    f.write("Project for the Subject Programming and Scripting \n \n")
    f.write("Author: Cecilia Pastore \n ")
    f.write("iris_analysis.txt \n \n")
    # check the first 5 line of the dataset to see if the format fit
    f.write("==== First 5 line of the dataset ==== \n \n")
    f.write(str(df.head()) + '\n \n')
    # print unique value on the the species colume to check no duplicate and that the replace has been done correctly 
    f.write("==== Print unique value of species ==== \n \n")
    f.write(str(df.drop_duplicates(subset ="Species"))+ '\n \n')
    # shape of the datased
    f.write("==== Shape of the dataset ==== \n \n")
    f.write("Number of rows: {}\n".format(df.shape[0]))
    f.write("Number of columns: {}\n".format(df.shape[1]))
    f.write("Size: {}\n".format(df.size))
    f.write("Columns: {}\n\n".format(", ".join(df.columns)))
    # get the data type 
    f.write("==== Data type ==== \n \n")
    f.write("Attribute \t \t \t \t Type \n \n")
    f.write(str(df.dtypes)+'\n\n')
    # get counts 
    f.write("==== Value Counts ==== \n \n")
    f.write("Species \t \t Count \n")
    f.write(str(df["Species"].value_counts())+'\n\n')
    # get statistics 
    f.write("==== Statistics ==== \n \n")
    f.write(str(df.describe())+'\n\n')
     # get an user more friendly view of the statistc 
    f.write("==== Mean/std per sciepes ==== \n \n")
    f.write(str(df.describe())+'\n\n')
   
