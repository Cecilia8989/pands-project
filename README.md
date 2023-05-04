 <h1 align="center">pands-project2023</h1>
 <h2 align="center">Iris Dataset</h2>

  <p align="center">
   Cecilia Pastore 

<details>
    <summary> Project assignement </summary>
           <p>

<h3 align="center"> Problem statement </h2>
 
>This project concerns the well-known Fisher’s Iris data set [3]. You must research the data set
and write documentation and code (in Python [1]) to investigate it. An online search for
information on the data set will convince you that many people have investigated it
previously. You are expected to be able to break this project into several smaller tasks that
are easier to solve, and to plug these together after they have been completed.

>You might do that for this project as follows:
> 1. Research the data set online and write a summary about it in your README.
> 2. Download the data set and add it to your repository.
> 3. Write a program called analysis.py that:
> 4. Outputs a summary of each variable to a single text file,
> 5. Saves a histogram of each variable to png files, and
> 6. Outputs a scatter plot of each pair of variables.
> 7. Performs any other analysis you think is appropriate
 
>You may produce a Jupyter notebook as well containing all your comment. This notebook
should only contain text that you have written yourself, (it may contain referenced code
from other sources). I will harshly mark any text (not code) that I feel is not written directly
by you. I want to know what YOU think, not some third party.
>It might help to suppose that your manager has asked you to investigate the data set, with a
view to explaining it to your colleagues. Imagine that you are to give a presentation on the
data set in a few weeks’ time, where you explain what investigating a data set entails and how
Python can be used to do it. You have not been asked to create a deck of presentation slides,
but rather to present your code and its output to them. 
 

</p>
</details>

### Iris Flower Datases - introduction 
The iris flower dataset is a well-known dataset in the field of data science, and it is often used to illustrate basic data analysis, visualization techniques and machine learning .  The Iris Dataset is considered as the "Hello World" for data science [[Fig.1]](https://machinelearninghd.com/iris-dataset-uci-machine-learning-repository-project/).

<p align="center">
  <img src=https://machinelearninghd.com/wp-content/uploads/2021/03/iris-dataset.png>
</p>

The dataset contains measurements of the sepal length, sepal width, petal length, and petal width for 150 iris flowers belonging to three different species: Iris setosa, Iris versicolor, and Iris virginica. Fifty samples are collected for each species [[Fig.2]](https://www.bogotobogo.com/python/scikit-learn/scikit_machine_learning_features_extraction.php).

The iris flower dataset was originally collected by the botanist Edgar Anderson in the 1930s and later popularized by the statistician Ronald Fisher in his seminal paper on discriminant analysis. The dataset is sometimes referred to as Anderson's Iris dataset, as Anderson collected it to quantify the morphological variations among three closely related Iris species. Anderson ensured that all of the samples were collected from the same pasture on the Gaspé Peninsula, on the same day, and measured at the same time by the same person using the same apparatus [[1]](https://rpubs.com/AjinkyaUC/Iris_DataSet).

Since then, the dataset has become a classic example in the field of data science, and it is frequently used in introductory courses and textbooks. It is a simple and well-understood dataset, making it a popular choice for teaching and research purposes, providing an excellent opportunity to explore different aspects of data analysis and visualization.

The dataset is widely available and can be accessed freely on the [UCI website [2]](https://archive.ics.uci.edu/ml/datasets/iris).

<p align="center">
  <img src=https://www.bogotobogo.com/python/scikit-learn/images/features/iris-data-set.png>
</p>


<h3> Import dataset </h3>

#### Import data set from an online location to a csv 

As a first task, The dataset need to be imported and transformed in a CSV [[3]](https://www.angela1c.com/projects/iris_project/downloading-iris/).
I have:
- imported the iris dataset from the [UCI Machine learning repository](http://archive.ics.uci.edu/ml/machine-learning-databases/iris/) in data format
- changed the column names to correspond with the attribute information in a nice format
- and saved the dataset as a CSV 

To avoid having Python download the dataset every time the main script is executed, I created a separate script called **downloadiris.py**.


<details>
    <summary> Code Explanation </summary>
           <p>
            
Import the Pandas library. 
Pandas [[4]](https://www.w3schools.com/python/pandas/default.asp) is a powerful library with many functions for analyzing data, and in this case, it will be used to read the file as a CSV.

```python
import pandas as pd 
```
Define the URL from which to download the dataset from the UCI Machine Learning Repository.
```python
csv_ulr =  'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
```
The dataset downloaded from csv_url does not contain any column names that match the attribute information. Therefore, we manually define column names.

```python
col_names = ['SepalLenght(cm)', 'SepalWidth(cm)', 'PetalLenght(cm)', 'PetalWidth(cm)', 'Species']
```
Using Panda library to download the dataset as a CSV and set the colums name.

```python
col_names = iris =  pd.read_csv(csv_ulr, names = col_names)
```
Save the CSV file and print a message to show the code have been execute correctly.

```python
iris.to_csv("iris_dataset.csv", index=False)
print("iris_dataset.csv created")
```
</p>
</details>

#### Import  the dataset from the CSV to the main script and adjust his foramt.

After saving the dataset from an online location as a CSV file in the same repository, we need to import it into our main script and adjust its format for further analysis. 

To do this, we can begin by importing the necessary libraries at the start of our script. 
We then import and define the dataset in the scrip and adjust the column/species names to a more readable format.  

##### *Import the libraries*

For this script we will use the the following libraries:

- pandas: a library for data manipulation and analysis
- NumPy: a library for numerical operations on arrays and matrices
- Matplotlib.pyplot: a plotting library for creating plot
- PyLab: a library that combines Matplotlib with NumPy functionality
- Seaborn: a library for creating informative and attractive statistical graphics

<details>
    <summary> Code </summary>

```python
# import needed libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
import seaborn as sns 
```  
</p>
</details>

##### *Import the dataset from the CSV file*

The first part of the script is to define and import the dataset from the CSV file. 
This has been done using pandas library's read_csv() function [[5]](https://realpython.com/python-csv/#reading-csv-files-with-pandas). The dataset is stored in the DataFrame called 'df'.

<details>
    <summary> Code </summary>
           <p>
            
```python
# import data from a csv file using pandas 
df = pd.read_csv('iris_dataset.csv')
```
</p>
</details>

##### *Change the series name*

The code then replaces the names of the three species with more friendly names using the replace() method of the Series object representing the "Species" column[[6]](https://datagy.io/pandas-replace-values/).
The 'to_replace' parameter specifies the value to be replaced, while the 'value' parameter specifies the new value.

<details>
    <summary> Code </summary>
           <p>

```python
# replace the 3 spieces with a more friendly name 
df["Species"].replace(to_replace="Iris-setosa", value="Setosa", inplace=True)
df["Species"].replace(to_replace="Iris-versicolor", value="Versicolor", inplace=True)
df["Species"].replace(to_replace="Iris-virginica", value="Virginica", inplace=True)
```
</p>
</details>



<details>
    <summary>Sources</summary>
           <p>

 - [1] [rpubs](https://rpubs.com/AjinkyaUC/Iris_DataSet)
 - [2] [UCI Machine Learning repository](https://archive.ics.uci.edu/ml/datasets/iris)
 - [3] [Importing and viewing the Iris dataset using pandas](https://www.angela1c.com/projects/iris_project/downloading-iris/) 
 - [4] [Pandas Tutorial](https://www.w3schools.com/python/pandas/default.asp)
 - [5] [Reading and Writing CSV Files in Python](https://realpython.com/python-csv/#reading-csv-files-with-pandas)
 - [6] [Pandas replace() – Replace Values in Pandas Dataframe](https://datagy.io/pandas-replace-values/)
 - [7] [](https://datagy.io/pandas-replace-values/)         
 - [6] []()
 - [7] []()               
 - [Fig.1] [Iris Dataset Project from UCI Machine Learning Repository](https://machinelearninghd.com/iris-dataset-uci-machine-learning-repository-project/)
 - [Fig.2] [Machine Learning 101](https://www.bogotobogo.com/python/scikit-learn/scikit_machine_learning_features_extraction.php)

</p>
</details>
 
