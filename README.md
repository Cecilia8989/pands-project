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
>    - Outputs a summary of each variable to a single text file,
>    - Saves a histogram of each variable to png files, and
>    - Outputs a scatter plot of each pair of variables.
>    - Performs any other analysis you think is appropriate
 
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

## Table of content
1. [Introduction](https://github.com/Cecilia8989/pands-project/blob/main/README.md#1-introduction)
   * [Technologies](https://github.com/Cecilia8989/pands-project/blob/main/README.md#technologies)
   * [Running the Script](https://github.com/Cecilia8989/pands-project/blob/main/README.md#running-the-script)
2. [Iris Flower Datases](https://github.com/Cecilia8989/pands-project/blob/main/README.md#2-iris-flower-datases)
3. [Import the dataset](https://github.com/Cecilia8989/pands-project/blob/main/README.md#3-import-the-dataset)
   * [Import data set from an online location to a csv](https://github.com/Cecilia8989/pands-project/blob/main/README.md#import-data-set-from-an-online-location-to-a-csv)
   * [Import the dataset from the CSV to the main script and adjust his format](https://github.com/Cecilia8989/pands-project/blob/main/README.md#import-the-dataset-from-the-csv-to-the-main-script-and-adjust-his-format)
4. [Exploring the Dataset](https://github.com/Cecilia8989/pands-project/blob/main/README.md#4-exploring-the-dataset)
   * [Creation and introduction](https://github.com/Cecilia8989/pands-project/blob/main/README.md#creation-and-introduction)
   * [Checking how appear the data in the Dataset](https://github.com/Cecilia8989/pands-project/blob/main/README.md#checking-how-appear-the-data-in-the-dataset)
   * [Unique values](https://github.com/Cecilia8989/pands-project/blob/main/README.md#unique-values)
   * [Missing values](https://github.com/Cecilia8989/pands-project/blob/main/README.md#missing-values)
   * [Shape of the dataset](https://github.com/Cecilia8989/pands-project/blob/main/README.md#shape-of-the-dataset)
   * [Data Type](https://github.com/Cecilia8989/pands-project/blob/main/README.md#data-type)
   * [Statistics](https://github.com/Cecilia8989/pands-project/blob/main/README.md#statistics)
   * [Statistics grouped by species](https://github.com/Cecilia8989/pands-project/blob/main/README.md#statistics-grouped-by-species)
   * [Quartiles per species](https://github.com/Cecilia8989/pands-project/blob/main/README.md#quartiles-per-species)
5. [Univariate analysis](https://github.com/Cecilia8989/pands-project/blob/main/README.md#5-univariate-analysis)
   * [Distribution Pie](https://github.com/Cecilia8989/pands-project/blob/main/README.md#distribution-pie)
   * [Histograms](https://github.com/Cecilia8989/pands-project/blob/main/README.md#histograms)
   * [Violin and Box Plots](https://github.com/Cecilia8989/pands-project/blob/main/README.md#violin-and-box-plots)
6. [Bivariate analysis](https://github.com/Cecilia8989/pands-project/blob/main/README.md#6-bivariate-analysis)
   * [Scatter Plot](https://github.com/Cecilia8989/pands-project/blob/main/README.md#scatter-plot)
   * [Pair Plot](https://github.com/Cecilia8989/pands-project/blob/main/README.md#pair-plot)
   * [Heat map](https://github.com/Cecilia8989/pands-project/blob/main/README.md#heat-map)
7. [Source](https://github.com/Cecilia8989/pands-project/blob/main/README.md#7-sources)


## 1. Introduction 

This code is a Python script to analyze the Iris flower dataset. The iris dataset is first downloaded from a URL by running the script downloadiris.py, and then analyzed with the script analysis.py. In analysis.py, the dataset is first imported and a summary of the dataset is printed in a text file. This summary contains unique values of species, missing values, dataset shape, data types, and statistics. For each species, the script calculates mean, median, standard deviation, minimum, and maximum, as well as the quartiles. Next, a Univariate Analysis is conducted using histograms, box plots, and violin plots. Finally, a Bivariate Analysis is conducted using scatter plots and a heatmap.

### Technologies 

- Phyton 3.19    

###  Running the Script

To use the code contained in this Project, make sure you have phyton an the required libraries installed on your system.  
To install them you can use pip install in a terminal or command prompt.

```python
pip install pandas matplotlib seaborn
```
To run the script, save the 2 scripts, open a terminal or command prompt and navigate to the directory where the script are saved. Then, run first the *downloadiris.py* and after *iris_analysis.py*:

```python
python downloadiris.py
python iris_analysis.py
```
The programs will create in the same repository a CSV file, a text file and several image.



## 2. Iris Flower Datases 
The iris flower dataset is a well-known dataset in the field of data science, and it is often used to illustrate basic data analysis, visualization techniques and machine learning .  The Iris Dataset is considered as the "Hello World" for data science [[Fig.1]](https://machinelearninghd.com/iris-dataset-uci-machine-learning-repository-project/).

<p align="center">
  <img src=https://machinelearninghd.com/wp-content/uploads/2021/03/iris-dataset.png>
</p>

The dataset contains measurements of the sepal length, sepal width, petal length, and petal width for 150 iris flowers belonging to three different species: Iris setosa, Iris versicolor, and Iris virginica. Fifty samples are collected for each species [[Fig.2]](https://www.bogotobogo.com/python/scikit-learn/scikit_machine_learning_features_extraction.php).

<p align="center">
  <img src=https://www.bogotobogo.com/python/scikit-learn/images/features/iris-data-set.png>
</p>

The iris flower dataset was originally collected by the botanist Edgar Anderson in the 1930s and later popularized by the statistician Ronald Fisher in his seminal paper on discriminant analysis. The dataset is sometimes referred to as Anderson's Iris dataset, as Anderson collected it to quantify the morphological variations among three closely related Iris species. Anderson ensured that all of the samples were collected from the same pasture on the Gaspé Peninsula, on the same day, and measured at the same time by the same person using the same apparatus [[1]](https://rpubs.com/AjinkyaUC/Iris_DataSet).

Since then, the dataset has become a classic example in the field of data science, and it is frequently used in introductory courses and textbooks. It is a simple and well-understood dataset, making it a popular choice for teaching and research purposes, providing an excellent opportunity to explore different aspects of data analysis and visualization.

The dataset is widely available and can be accessed freely on the [UCI website [2]](https://archive.ics.uci.edu/ml/datasets/iris).

## 3. Import the dataset 

### Import data set from an online location to a csv 

As a first task, [The dataset need to be imported from an URL and transformed in a CSV [3]](https://www.angela1c.com/projects/iris_project/downloading-iris/).
I have:
- imported the iris dataset from the [UCI Machine learning repository](http://archive.ics.uci.edu/ml/machine-learning-databases/iris/) in data format
- changed the column names to correspond with the attribute information in a nice format
- and saved the dataset as a CSV 

To avoid having Python download the dataset every time the main script is executed, I created a separate script called **downloadiris.py**.


<details>
    <summary> Code Explanation </summary>
           <p>
            
Import the Pandas library. 
[Pandas [4]](https://www.w3schools.com/python/pandas/default.asp) is a powerful library with many functions for analyzing data, and in this case, it will be used to read the file as a CSV.

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

### Import the dataset from the CSV to the main script and adjust his format

After saving the dataset from an online location as a CSV file in the same repository, we need to import it into our main script and adjust its format for further analysis. 

To do this, we can begin by importing the necessary libraries at the start of our script. 
We then import and define the dataset in the scrip and adjust the species names to a more readable format.  

#### *Import the libraries*

For this script we will use the the following libraries:

- Pandas: a library for data manipulation and analysis
- Matplotlib.pyplot: a library for creating plot
- [Seaborn [5]]( https://seaborn.pydata.org/tutorial/introduction): a library for creating informative and attractive statistical graphics

<details>
    <summary> Code </summary>

```python
# import needed libraries 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```  
</p>
</details>

#### *Import the dataset from the CSV file*

The first part of the script is to define and import the dataset from the CSV file. 
This has been done using pandas library's [*read_csv() function* [6]](https://realpython.com/python-csv/#reading-csv-files-with-pandas). The dataset is stored in the DataFrame called *df*.

<details>
    <summary> Code </summary>
           <p>
            
```python
# import data from a csv file using pandas 
df = pd.read_csv('iris_dataset.csv')
```
</p>
</details>

#### *Change the series name*

The code then replaces the names of the three species with more friendly names using the [*replace() method* [7]](https://datagy.io/pandas-replace-values/) of the Series object representing the "Species" column.
The *to_replace* parameter specifies the value to be replaced, while the *value* parameter specifies the new value.

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

## 4. Exploring the Dataset

Once the dataset have been imported and formatted in the needed way, we will need to explore it and prepare it for analysis. This analysis of the information contained in the dataset, as requested, will be printed in a text file called *iris_summary.txt*.

### Creation and introduction 

Initially the code opens a  file (and create it if is not already created) named *iris_summary.txt* in write mode. The subsequent lines of code write an introduction to the file, including the author's name and the title of the project.

```
Project for the Subject Programming and Scripting 
 
Author: Cecilia Pastore 
 iris_summary.txt
```
</p>
</details>

<details>
    <summary> Code explanation </summary>
           <p>

The code is creating a new file named *iris_summary.txt* and opening it in write mode using the [*open()* function [8]](https://datagy.io/python-write-text-file/), with the file being assigned to the variable *f*. The code then writes some introductory information about the text file, including the project title, author name, and the name of the text file itself.

```python
# create the text file and write on them 
with open ('iris_analysis.txt', 'w') as f:
    # print an introduction of the text file 
    f.write("Project for the Subject Programming and Scripting \n \n")
    f.write("Author: Cecilia Pastore \n ")
    f.write("iris_analysis.txt \n \n")   
```

</p>
</details>
 
### Checking how appear the data in the Dataset 

Now, we can take a look on how the Data-Set look like printing the first 5 lines of it. 

```
==== First 5 lines of the dataset ==== 
 
   SepalLenght(cm)  SepalWidth(cm)  PetalLenght(cm)  PetalWidth(cm) Species
0              5.1             3.5              1.4             0.2  Setosa
1              4.9             3.0              1.4             0.2  Setosa
2              4.7             3.2              1.3             0.2  Setosa
3              4.6             3.1              1.5             0.2  Setosa
4              5.0             3.6              1.4             0.2  Setosa
```

<details>
    <summary> Code Explanation </summary>
           <p>
            
The [*df.head()* [9]](https://www.geeksforgeeks.org/python-pandas-dataframe-series-head-method/) function have been used to display the first 5 rows of the df dataset, and then converts the output to a string using *str()*. The resulting string is then written to the file using the *f.write()* function.


```python
    # checking the first 5 line of the dataset to see if the format fit
    f.write("==== First 5 line of the dataset ==== \n \n")
    f.write(str(df.head())+'\n \n')
```

</p>
</details>

### Unique values

We can now print the unique values of the *Species* column. This serves the dual purpose of checking that no duplicate species have been entered and verifying that the renaming of the species has been carried out correctly. As we can see from the output, there are no values other than the three desired species, and the renaming has been executed correctly.

```
==== Print unique value of species ==== 
 
Species
 
Setosa
Versicolor
Virginica
```

<details>
    <summary> Code Explanation </summary>
           <p>

The script defines a variable *unique_species* that contains the unique values in the *Species* column of the dataset. I would have been to do it through the use of [*drop.duplicate()* function [10]](https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/) or through the [*unique()* function [11]](https://www.projectpro.io/recipes/list-unique-values-in-pandas-dataframe). I chose to unique function to give a more tidy looking on the text file. 
Then, it writes these values in the text file using a for loop to display the values in a more readable format. The output is a list of unique species names, with each species name on a separate line, and the text "Species" written at the beginning to clarify the content of the list.

```python
    # print unique value on the the species colume to check no duplicate and that the replace has been done correctly 
    f.write("==== Print unique value of species ==== \n \n")
    unique_species = pd.unique(df['Species'])
    f.write("Species\n \n")
    for species in unique_species:
        f.write(species)
        f.write("\n")
    f.write("\n")
```

</p>
</details>

### Missing values 

The script will check if there are [missing value or not [10]](https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/). Missing values refer to the absence of data or information for one or more items or a whole unit. It can happen when the data is not provided, is lost or simply does not exist. We can see from the output that no column as any missing value. This was expected ad the iris dataset is know to not have them.

```
==== Checking missing value ==== 
 
SepalLenght(cm)    0
SepalWidth(cm)     0
PetalLenght(cm)    0
PetalWidth(cm)     0
Species            0
dtype: int64
```

<details>
    <summary> Code Explanation </summary>
           <p>

The script check missing value using the [*isnull()* function [10]](https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/).

```python
    # checking missing value
    f.write("==== Checking missing value ==== \n \n")
    f.write(str(df.isnull().sum())+'\n \n')  
```

</p>
</details>

### Shape of the dataset 

The script prints the shape of the dataset, which is the number of rows and columns in the dataset. It also prints the size of the dataset, which is the product of the number of rows and columns and a list of all the column names in the dataset. 
Finally it show the number on entries for each species.
As we can see we have 150 lines, 5 columns for a total size of 750 entries. Each specie has 50 entries.

```
==== Shape of the dataset ==== 
 
Number of rows: 150
Number of columns: 5
Size: 750
Columns: SepalLenght(cm), SepalWidth(cm), PetalLenght(cm), PetalWidth(cm), Species

Species
Setosa        50
Versicolor    50
Virginica     50
dtype: int64
```

<details>
    <summary> Code Explanation </summary>
           <p>

The script retrieve various information about a dataset. It first uses the [*shape()* [12]](https://stackoverflow.com/questions/58008120/how-to-use-format-in-python-to-print-out-the-data-shape) function to print the number of rows and columns in the dataset. Then, it uses the *size()* function to print the total number of entries in the dataset. The [*join()* [13]](https://sparkbyexamples.com/pandas/pandas-join-dataframes-on-columns/) function is used to concatenate the names of all columns in the dataset and print them. 
Finally, the [*value_counts()* [10]](https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/) function is used to count the number of entries for each species in the dataset and print them.

```python
    # shape of the datased
    f.write("==== Shape of the dataset ==== \n \n")
    f.write("Number of rows: {}\n".format(df.shape[0]))
    f.write("Number of columns: {}\n".format(df.shape[1]))
    f.write("Size: {}\n".format(df.size))
    f.write("Columns: {}\n\n".format(", ".join(df.columns)))
    f.write(str(df.value_counts("Species"))+'\n\n')
```

</p>
</details>
 
### Data Type 
 
Next, the script checks the data type of each column in the dataset. It outputs this information in the text file, with each column name followed by its corresponding data type. As we can see, the data type of all columns is float except for the *Species* column, which is an object datatype that contains the species referred to in the measurements.

```
==== Data type ==== 
 
Attribute 	 	 	 	 Type 
 
SepalLenght(cm)    float64
SepalWidth(cm)     float64
PetalLenght(cm)    float64
PetalWidth(cm)     float64
Species             object
dtype: object
```

<details>
    <summary> Code Explanation </summary>
           <p>

The code use the [*dtypes* [14]](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dtypes.html) function to get the type of each columns.

```python
    # get the data type 
    f.write("==== Data type ==== \n \n")
    f.write("Attribute \t \t \t \t Type \n \n")
    f.write(str(df.dtypes)+'\n\n') 
```

</p>
</details>

### Statistics

Some descriptive statistics for each column of the dataset are provided. It includes the count, mean, standard deviation, minimum, maximum, and quartile values for numeric columns. This is done through the [*describe()* function [15]](https://www.w3resource.com/pandas/dataframe/dataframe-describe.php).

```
==== Statistics ==== 
 
       SepalLenght(cm)  SepalWidth(cm)  PetalLenght(cm)  PetalWidth(cm)
count       150.000000      150.000000       150.000000      150.000000
mean          5.843333        3.054000         3.758667        1.198667
std           0.828066        0.433594         1.764420        0.763161
min           4.300000        2.000000         1.000000        0.100000
25%           5.100000        2.800000         1.600000        0.300000
50%           5.800000        3.000000         4.350000        1.300000
75%           6.400000        3.300000         5.100000        1.800000
max           7.900000        4.400000         6.900000        2.500000
```

<details>
    <summary> Code Explanation </summary>
           <p>

The *describe()* function is used to calculate the count, mean, standard deviation, minimum, maximum, and quartile values for the numeric columns of the dataset. 

```python
    # get statistics 
    f.write("==== Statistics ==== \n \n")
    f.write(str(df.describe())+'\n\n') 
```

</p>
</details>

### Statistics grouped by species

Next I want to check the statistics (mean, mediam, std, min and max) for each species.

```
==== SepalLenght(cm) Statistics ====

             mean  median       std  min  max
Species                                      
Setosa      5.006     5.0  0.352490  4.3  5.8
Versicolor  5.936     5.9  0.516171  4.9  7.0
Virginica   6.588     6.5  0.635880  4.9  7.9

==== SepalWidth(cm) Statistics ====

             mean  median       std  min  max
Species                                      
Setosa      3.418     3.4  0.381024  2.3  4.4
Versicolor  2.770     2.8  0.313798  2.0  3.4
Virginica   2.974     3.0  0.322497  2.2  3.8

==== PetalLenght(cm) Statistics ====

             mean  median       std  min  max
Species                                      
Setosa      1.464    1.50  0.173511  1.0  1.9
Versicolor  4.260    4.35  0.469911  3.0  5.1
Virginica   5.552    5.55  0.551895  4.5  6.9

==== PetalWidth(cm) Statistics ====

             mean  median       std  min  max
Species                                      
Setosa      0.244     0.2  0.107210  0.1  0.6
Versicolor  1.326     1.3  0.197753  1.0  1.8
Virginica   2.026     2.0  0.274650  1.4  2.5

```

<details>
    <summary> Code Explanation </summary>
           <p>

This script loops through all columns except for the last one (the species one), and for each column, it calculates the mean, median, standard deviation, minimum, and maximum value for each species in the dataset. It does this by using the [*groupby()* [16]](https://learnpython.com/blog/how-to-summarize-data-in-python/) function to group the data by species, and then using the [*agg()* [17]](https://www.w3schools.com/python/pandas/ref_df_agg.asp) function to apply the statistical functions to each group. 

```python
    # get an user more friendly view of the statistics 
    # for loop to print for each species the varaible mean, median, std, min, max 
    for column in df.columns[:-1]:
        f.write(f"==== {column} Statistics ====\n\n")
        f.write(f"{df.groupby('Species')[column].agg(['mean', 'median', 'std', 'min', 'max'])}\n\n")
```

</p>
</details>
 
### Quartiles per species 

I wanted now chech the quartiles value of each species/variable.

```
==== Quartiles per species ==== 
 
                 SepalLenght(cm)  SepalWidth(cm)  PetalLenght(cm)  PetalWidth(cm)
Species                                                                          
Setosa     0.25            4.800           3.125            1.400             0.2
           0.50            5.000           3.400            1.500             0.2
           0.75            5.200           3.675            1.575             0.3
Versicolor 0.25            5.600           2.525            4.000             1.2
           0.50            5.900           2.800            4.350             1.3
           0.75            6.300           3.000            4.600             1.5
Virginica  0.25            6.225           2.800            5.100             1.8
           0.50            6.500           3.000            5.550             2.0
           0.75            6.900           3.175            5.875             2.3
```

<details>
    <summary> Code Explanation </summary>
           <p>

This code calculates the quartiles for each species in the dataset using the *groupby* function. The *groupby* function groups the data by the Species column, and then the *quantile* function is applied to each group. The [*quantile* function is given a list of values [0.25, 0.50, 0.75] [18]](https://stackoverflow.com/questions/55009203/how-does-pandas-calculate-quartiles) which represent the quartiles that we want to calculate for each group . 

```python
    # get quartile per species 
    f.write("==== Quartiles per species ==== \n \n")
    f.write(str(df.groupby('Species').quantile([0.25, 0.50, 0.75]))+'\n\n')   
```

</p>
</details>

## 5. Univariate analysis

[Univariate analysis [19]](https://www.kaggle.com/code/amrut11/iris-dataset-univariate-bivariate-multivariate) explores only one dependent variable. "Uni" means "one," and the main purpose is to describe a dataset, summarize the data, and find the patterns present in it. When a dataset contains multiple variables, each of them is explored separately. We will explore several types of plots that are used for this kind of analysis.

### Distribution Pie 

As a first visualization I would like to start with a pie chart to visualize the distribution of the different species in the dataset. This cake graphic show that each species has 50 entries in a donut format.

![pie Chart](https://github.com/Cecilia8989/pands-project/blob/main/Plot1_PieOfDistribution.png)

<details>
    <summary> Code Explanation </summary>
           <p>

This code will plot a [pie chart and inside will plot a white circle to give the design of a donut[20]](https://plainenglish.io/blog/how-to-make-a-beautiful-donut-chart-and-nested-donut-chart-in-matplotlib-92040c8bbeea).

First, it uses the *value_counts()* function to count the number of occurrences of each species in the Species column of the DataFrame. The resulting counts are stored in the *group_count* variable.
Next, it uses the [unique() [21]](https://sparkbyexamples.com/pandas/pandas-find-unique-values-from-columns/) function to get an array of the unique species in the Species column of the DataFrame. The resulting array is stored in the labels variable.

```python
# create a pie chart to show the distribution of species 
# get the count of each species
group_count= df['Species'].value_counts()
# define the labels of the pie chart
labels= df['Species'].unique()
```
The script utilizes the *pie()* function from the Matplotlib library to generate a pie chart. The *group_count* and [*labels* [22]]( https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html) variables are defined to plot the chart and passed as arguments in the *pie()* function. The script also defines the size and position of the chart, as well as the formatting of the percentage labels and the appearance of the wedges. 

```python
# set the parameters of the pie chart
plt.pie(group_count, labels=labels, autopct='%1.0f%%', 
        textprops={'fontsize': 14, 'fontweight': 'bold'},
        wedgeprops={'linewidth': 2, 'edgecolor': 'white', 'alpha':0.7})
```
A white circle is created in the middle of the pie chart to give the design of a [donut [20]](https://plainenglish.io/blog/how-to-make-a-beautiful-donut-chart-and-nested-donut-chart-in-matplotlib-92040c8bbeea) with the following functions:

- plt.Circle(() creates a white which is added to the center of the pie chart.

- fig = plt.gcf() gets the current figure.

- fig.gca().add_artist(centre_circle) adds the white circle to the figure.

- plt.axis('equal') makes sure that the x and y axes have the same scale, so the pie chart appears circular.

```python
# create a white cirle to have the donut effect 
centre_circle= plt.Circle((0,0),0.40,color='white', fc='white',linewidth=1.00)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.axis('equal')
```
Finally a title, and is format, is defined and the plot is saved as a figure.

```python
# print a title
plt.title('Distribution of Species', color='Red', fontweight='bold', fontsize=20)
# save the plot as immage 
plt.savefig("Plot1_PieOfDistribution.png")
```

</p>
</details>

### Histograms

An histogram is a graph that allows us to explore the frequency distribution of a numerical variable. The X-Axis represents a range of values grouped together that we want to investigate, while the Y-Axis represents the frequency or count of data for each value.

First I would like to start with an histogram showing the mean of each variables for each species.  

![Hist-1](https://github.com/Cecilia8989/pands-project/blob/main/Plot2_AverageBar.png)

**Observation:**
As we can see, The species Virginica had higher mean values for Sepal length, Petal length, and Petal width compared to the other two species (Setosa and Versicolor). On the other hand, Setosa had the highest mean value for Sepal width.

<details>
    <summary> Code Explanation </summary>
           <p>

The code calculate the mean value for each species using the *groupby() method* and stores them in a variable called *class_averages*. 
It also set up the dark style from the [seaborn library [23]](https://www.educba.com/seaborn-styles/). 


```python
# Create a bar plot with the mean of each categories per species [4]
# Compute the average of each feature for each class
class_averages = df.groupby('Species').mean()
# select a seaborn style 
sns.set_style("dark")  
```
This variable *class_averages* is then used as the input for the [*plot()* method function [24]](https://www.shanelynn.ie/bar-plots-in-python-using-pandas-dataframes/) to create a bar chart. The *kind* parameter is set to *bar* to specify that a bar chart should be created. The *alpha* parameter is set to 0.7 to adjust the transparency of the bars.
Finally, title and label name is defined.
            
```python
# Create the bar chart
class_averages.plot(kind='bar', alpha=0.7)
plt. title('Iris Feature Averages by Species', fontweight = 'bold', fontsize = 20)
plt. xlabel('Species', fontweight = 'bold', fontsize = 14)
plt. ylabel('Average', fontweight = 'bold', fontsize = 14)   
```
The code rotate the X labels using the [*xticks()* function [25]]( https://stackabuse.com/rotate-axis-labels-in-matplotlib/) and save the plot as the figure *Plot2_AverageBar*.
```python
# rotate the x values [5]
plt.xticks(rotation=0)
plt.savefig('Plot2_AverageBar')   
```

</p>
</details
 
Next, I want the code plot an histogram for each variable separately to show the distribution of values for each species. Instead of creating four separate graphs, the code combine them into one figure using subplots. The histogram for each variable is created using seaborn's [*histplot()* method [26]](https://stackoverflow.com/questions/67300148/best-fit-to-a-histogramplot-iris), which includes a KDE curve (kernel density estimation) and shows the distribution of values for each species using a different color. 

![Bar](https://github.com/Cecilia8989/pands-project/blob/main/Plot3_Subplot_FeaturesBar.png)

**Observation:** 
Plot 1 and 2 show that there is a significant amount of overlap between the species on sepal length and sepal width. Both of this feature are not an effective Classification feature.

Plot 3 reveals a clearer distinction between the different species of iris. While there is some partial overlap between the Versicolor and Virginica species, Setosa is distinctly separated from the other two. 

Plot 4 shows a clearer distinction between the different species than Plot 3. The overlap between Versicolor and Virginica is further reduced in Plot 4, and Setosa is again well separated from the other two species.

To summarize, we can use Petal Length and Petal Width as the classification feature.
Focusing on Petal lenght, as the KVE curve of Setosa ends roughly at 2.1,if Petal Length is less than 2.1, the species is most likely Iris Setosa. The point of intersection between the KVE curves of Virginica and Versicolor is roughly at 4.8. This means that if Petal Length is between 2.1 and 4.8, the species is most likely Iris Versicolor. When the Petal Lenght is more than 4.8 then the specie is probably Virginica.
 
<details>
    <summary> Code Explanation </summary>
           <p>

This line converts the *Species* column in the DataFrame *df* to a categorical variable [[26]](https://stackoverflow.com/questions/67300148/best-fit-to-a-histogramplot-iris). This is useful for setting the order of the categories in plots.
 
```python
# make the 'species' column categorical to fix the order
df['Species'] = pd.Categorical(df['Species'])
```
This line creates a figure with a 2x2 grid of subplots, stored in the fig and axs variables.
```python
fig, axs = plt.subplots(2, 2, figsize=(12, 6))
# initialize a counter for the subplot index
```
Here the subplot is created. A loop interact with the first 4 columns of the dataframe [:4], using the *zip()* funtion to pair each column with its corresponding subplot. For each column and subplot, a histogram with a KDE curve is created using the *sns.histplot()* function. The *Species* column is used for the *hue*, which means that the histogram is plotted separately for each species. 
The title  of each plot and y label have been also added through [*ax.set* [27]](https://www.geeksforgeeks.org/matplotlib-axes-axes-set_xlabel-in-python/).

```python
i = 0
# loop through the first 4 columns of the DataFrame and corresponding subplots
for col, ax in zip(df.columns[:4], axs.flat):
    # create a histogram with a KDE curve for the current column, using the 'Species' column for the hue
    sns.histplot(data=df, x=col, y=None, kde=True, hue='Species', common_norm=False, legend=ax==axs[0,0], ax=ax)
    # set the title and the labels name
    ax.set_title(f'Plot {i+1} - {col}')
    ax.set_xlabel(None)
    ax.set_ylabel('Count')
    i = i+1
```
Finally a title of the subplot have been added using the *subtitle()* method. As the title of the subplot and single plot were overlapping [the position of the first have been adjusted [28]](https://www.statology.org/matplotlib-subplot-spacing/).
The figure have been then saved as *Plot3_Subplot_Feature*.

```python
# adjust the spacing between the subplots and set the figure title
fig.subplots_adjust(hspace=0.4, top=0.85, right=0.8)
fig.suptitle('Distribution of Iris Flower Features', fontsize=16, color='red', fontweight='bold')
# adjust the layout and save the figure  
plt.tight_layout()
plt.savefig("Plot3_Subplot_FeaturesBar.png")
```
</p>
</details>
 
### Violin and Box Plots 

Other data visualization techniques used to summarize and display the distribution of a dataset are the box pot and the violin pot.

A [box plot [29]](https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d)is a plot that shows the distribution of a dataset based on 5 keys values the minimum, the maximum value, the median (middle value), the first quartile (25%) and the third quartile (75%) value. 

A [violin [30]](https://mode.com/blog/violin-plot-examples/) is similar to a Box Plot but give more information about the the density estimated. It combines the feature of a box plot and a kernel density plot (which displays the density of the data). With a violin plot you can quickly see where most of the data is concentrated and how spread out it is.[[Fig.3]](http://www.sci.utah.edu/~kpotter/Library/Papers/hintze:1998:VPDT/index.html). 

![box_plot](http://www.sci.utah.edu/~kpotter/Library/Papers/hintze:1998:VPDT/hintze_1998_VPDT_00.png)

As both the visualization technique give similar information I have plot them together, one above the other:

![BoxPlotVioninPlot](https://github.com/Cecilia8989/pands-project/blob/main/Plot4_BoxAndViolinPlot.png)

**Observation:** The most significant variables, based on the graph above are petal length and petal width. For these variables, Setosa has a smaller range of values and less density compared to the other two species, while Versicolor has a moderate range and density. On the other hand, for sepal length and width, Virginica has a wider range of values and higher density compared to the other two species [[31]](https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-4df6f045cda).
 
he new set of plots supports the previous conclusion that Petal Length and Petal Width are the most significant variables for distinguishing between the three species of iris.

<details>
    <summary> Code Explanation </summary>
           <p>

The code creates a figure with [two subplots [32]](https://deepnote.com/@econdesousa/ViolinPlotvsBoxPlot-aadf0c53-53b4-4221-89b9-4388c54c68bd), one for violin plots and one for box plots . The number of plot for each line of the subplot are based on the number of columns of the data-set less 1 (len(df.columns)-1). The seaborn stile have been also changed in "darkgrid".

```python
# Create a subplots with 4 Violin plots and 4 box plots
# Create a figure with two subplots, one for each type of plot
sns.set_style("darkgrid")
fig, axs = plt.subplots(2, len(df.columns)-1, figsize=(20,10)) 
```
The first subplot is created. Through a for loop  an the *sns.violinplot()* function, 4 Violin plots are created, one for each variables grouped by *Species*. A color [palette [33]](https://www.practicalpythonfordatascience.com/ap_seaborn_palette) have been set. 
Additionally, the code also set up the y label and remove the x label. 

```python
# For loop to create a violin plot for each variable in the first row of subplots
for i in range (0, len(df.columns)-1):
    sns.violinplot(x='Species', y=df.columns[i], data=df, ax=axs[0,i], palette ='flare')
    # Define the format of the labels
    axs[0,i].set_ylabel(f'{df.columns[i]}', fontweight='bold')
    axs[0,i].set_xlabel(None)
```
The second subplot with 4 Box plots, one for each variables grouped by *Species*, is created on a similar way using the *sns.boxplot()* function. Labels are also defined and in this case, the X label has been left to be shown.

```python
# Create a box plot for each variable in the second row of subplots
for i in range (0, len(df.columns)-1):
    sns.boxplot(x='Species', y=df.columns[i], data=df, ax=axs[1,i],palette ='flare')
     # Define the format of the labels
    axs[1,i].set_ylabel(f'{df.columns[i]}', fontweight='bold')
    axs[1,i].set_xlabel('Species', fontweight='bold')
```
Finally, the title have been added, the layout adjusted and the graph saved as a picture.
 
```python
# Add a title of the plot      
plt.suptitle("Box and Violin plots for all the 4 variables", fontsize=20, fontweight='bold', color = 'red')
# Adding space on the top for the title
plt.subplots_adjust(top=0.95)  
# adjsut the layout and save the figure
plt.tight_layout() 
plt.savefig('Plot4_BoxAndViolinPlot.png')
```
</p> 
 </details>

## 6. Bivariate analysis

Bivariate analysis involve the study of two variables simultaneously to establish a relationship or correlation between them. The main objective of bivariate analysis is to determine whether there is any association between the two variables and the strength and direction of that association.   

 ### Scatter Plot 

A scatter plot is a way of representing data using dots on a two-dimensional graph [[29]](https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d). Each dot represents a pair of values for two different variables, with one variable plotted on the x-axis and the other variable plotted on the y-axis. The plot allows you to visualize the relationship between the two variables and identify any patterns or trends that may be present.
 
I have decided to create four scatter plots to examine the relationship between two variables for each plot (four combinations of features). All four plots have been combined into a single figure.

The output is a subplot with 4 scatter plots each exploring the relationship between 2 variables:
- Sepal Length and Width  
- Petal Length and Width 
- Sepal Length and Petal Width 
- Petal Length and Sepal Width

![Scatter](https://github.com/Cecilia8989/pands-project/blob/main/Plot5_scatterpoint.png)

Looking at the above figure, the scatter plot showing the relationship between Petal Length and Petal Width is the most useful in distinguishing between the three species of iris as they show distinct differences between petal sizes. Setosa species has the smallest petal lengths and widths, while the Virginica species has the largest, and the Versicolor species falls in between.

On the whole, with a very little overlaping between the species, Petal Length and Petal Width relationship can be useful features for distinguishing between the three species.

<details>
    <summary> Code Explanation </summary>
           <p>


The code creates a [subplot with four scatter plots [34]](https://www.kaggle.com/code/asimislam/tutorial-python-subplots) , comparing two features of the dataset for each subplot. It also sets the style of and the the size of the figure.

```python
# Create a supbplot with 4 scatterpoint comparing 2 features each 
fig = plt.figure(figsize=(14,7))
# Set the style of the plot to "darkgrid"
sns.set_style("darkgrid")  
```
Space in the subplot are adjusted and it is defined the title of the entire figure.

```python
# Adjust the space between subplots and the top margin of the figure
fig.subplots_adjust(hspace=0.4, top=0.85)
# Add a  title to the entire figure
plt.suptitle("Comparison between various Species", fontsize=18, color='red', fontweight='bold') 
```
The code creates four scatter plots, each comparing two different features (Sepal Length and Sepal Width, Petal Length and Petal Width, Petal Length and Sepal Width, and Petal Width and Sepal Length). The  subplot is created with [*plt.subplot()*[34]](https://www.kaggle.com/code/asimislam/tutorial-python-subplots) and the scatter plots are created using the [*sns.scatterplot()*[31]](https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-4df6f045cda) function, and the hue argument is set to the *"Species"*. 
```python
# Create the first scatter plot comparing Sepal Length and Sepal Width
plt.subplot(221)
plt.title("Sepal Lengh and Width", fontweight='bold')
sns.scatterplot(x=df['SepalLenght(cm)'], y=df['SepalWidth(cm)'], hue=df['Species'], s=80, alpha=0.8, palette="Dark2")

# Create the second scatter plot comparing Petal Length and Petal Width
plt.subplot(222)
plt.title("Petal Length and Width", fontweight='bold')
sns.scatterplot(x=df['PetalLenght(cm)'], y=df['PetalWidth(cm)'], hue=df['Species'], s=80, alpha=0.8, palette="Dark2", legend=False)

# Create the third scatter plot comparing Petal Length and Sepal Width
plt.subplot(223)
plt.title("Petal Length and Sepal Width", fontweight='bold')
sns.scatterplot(x=df['PetalLenght(cm)'], y=df['SepalLenght(cm)'], hue=df['Species'], s=80, alpha=0.8, palette="Dark2", legend=False)

# Create the fourth scatter plot comparing comparing Petal Width and Sepal Length
plt.subplot(224)
plt.title("Petal Widht and Sepal Lenght", fontweight='bold')
sns.scatterplot(x=df['PetalWidth(cm)'], y=df['SepalLenght(cm)'], hue=df['Species'], s=80, alpha=0.8, palette="Dark2", legend=False)
```
Finally, the layout is adjusted and the plot saved as a figure.

```python
# Adjust the layout and save the figure 
plt.tight_layout()
plt.savefig("Plot5_Subplot_scatterpoint.png")
```

</p>
 </details>

### Pair Plot
 
A Pair plot is a useful tool for visualizing the relationships between variables. It produce a matrix of scatter plots that show the relationship between each pair of variables in a dataset. It is create through the *sns.pairplot()* method.
 
![PairPlot](https://github.com/Cecilia8989/pands-project/blob/main/Plot6_all_paired%20attributes.png)

**Observation:** The analysis suggests that there is a strong positive correlation between petal length and Petal width, meaning that as one variable increases, the other variable tends to increase as well. Furthermore, the results indicate that Setosa has relatively low values for both petal length and width, while Versicolor has average values for both, and Virginica has high values for both. When it comes to sepal dimensions, the findings show that Setosa has high sepal width but low sepal length, Versicolor has average values for both sepal width and length, and Virginica has small width but large sepal length.
 
In summary, even when considering the relationship between all variables, the conclusion of the previous set of graphs is confirmed. Petal length and petal width are the most useful features for distinguishing between the three species.
 
<details>
    <summary> Code Explanation </summary>
           <p>

First, the code is adjusting font and the size of the labels, to have a plot more readable. This is done using the [sns.set_context() function [35]](https://stackoverflow.com/questions/45204552/how-to-change-size-of-axis-labels-and-values-in-seaborn-pairsplot).

```python
# Create a scatterplot of Scatterplots of all-paired attributes
# Set the context for the plot, adjusting the size of the labels and fonts
sns.set_context("paper", rc={"axes.labelsize":20})
sns.set_context("talk", font_scale=1.4)  
```
The Plot is created using the [*sns.parirplot* [28]](https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-4df6f045cda) function. The *height* argument set the heigh of each plot and the *palette* argument sets the color palette to be used in the plot. In this case, it is set to *colorblind*.

```python
# Create a pairplot of the dataset
sns.pairplot(df,hue='Species', height=4, palette = 'colorblind')  
```
This code adds a title to a figure and adjusts the top margin. It also saves the figure with the name *Plot5_all_paired attributes*.

```python
# Add a title to the entire figure, adjust the top margin and save the figure 
plt.suptitle("Scatterplots of all-paired attributes", fontsize=20, fontweight='bold', color = 'red')
plt.subplots_adjust(top=0.95)
plt.savefig("Plot5_all_paired attributes.png")  
```
</p>
 </details>
  
### Heat map 

Finally, the correlation between the variables can be explored using an heat map.

An heat map is a visual representation of data that uses color to show the relationships between numerical variables in a dataset. It's a simple way to plot and understand [correlations within variables [10]](https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/). 

![HeatMap](https://github.com/Cecilia8989/pands-project/blob/main/Plot7_heatmap.png)

**Observation:** 
 From the plot above we can see that petal width and petal length have an high correlations. 
 A good correlations result from:
- Petal length and pepal width 
- Petal Width and Sepal length 

On the other hand, Sepal width/Petal Length are the less correlated variables. 
 
 Again, the high correlation between petal width and petal length indicates that these two features provide similar information and are highly predictive in distinguishing between species of iris. Therefore, using either one of these features or both together can be effective in classification tasks.

<details>
    <summary> Code Explanation </summary>
           <p>

The code creates a figure with a specified size using *plt.subplots*, and then uses [*sns.heatmap* [36]](https://stackoverflow.com/questions/51568083/matplotlib-and-seaborn-heatmap-renders-differently-in-jupyter-to-savefig-labels)to create an heatmap of the given data . Several arguments are used, such as [*annot_kws* [37]](https://stackoverflow.com/questions/33104322/auto-adjust-font-size-in-seaborn-heatmap) to specify the format of the annotations, *alpha* to define the transparency, and [*cmap* [38]](https://www.analyticsvidhya.com/blog/2020/09/colormaps-matplotlib/) to define the color map. *yticklabels* and *xticklabels* are also defined to allow for modification of the labels on the x and y axes. 
```python
# Create an heatmap

# Create a figure with a specified size
fig, ax = plt.subplots(figsize=(11, 10))
# Create the heatmap with specified parameters
ax = sns.heatmap(df. corr(), 
            xticklabels=True,
            yticklabels=True,
            annot=True,
            cmap ='inferno',
            annot_kws={'fontsize': 14, 'fontweight':'bold'},
            alpha=0.9)  
```
The code define the format for the X-axi and Y-axi. For both the axes the size, the weight and rotation are defined. For the X-axi a 45 grade rotation have been defined.
Finally, A title of the graph is defined with the corresponding format. The [*pad* [39]](https://stackoverflow.com/questions/66226320/how-do-you-add-padding-between-the-x-axis-tick-marks-not-tick-labels-and-the-x) argument is used to add some space between the title and the graph.

```python
# Set the parameters for the y-axis labels
ax.set_yticklabels(ax.get_yticklabels(), rotation=0, fontsize=14, fontweight='bold')
# Set the parameters for the x-axis labels
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, fontsize=14, fontweight='bold', rotation_mode='anchor', ha='right')
# Set the title for the plot
ax.set_title("Correlation Matrix Heatmap", fontsize=24, fontweight='bold', color = 'red' , pad=40)
```
Finally the layout is adjusted and the figure saved.

```python
# Adjust the layout and save the plot 
fig.tight_layout()
fig.savefig('Plot6_heatmap.png')   
```

</p>
</details>
 
 ## 7. Sources
 <details>
    <summary>References</summary>
           <p>
            
 - [1] [rpubs](https://rpubs.com/AjinkyaUC/Iris_DataSet)
 - [2] [UCI Machine Learning repository](https://archive.ics.uci.edu/ml/datasets/iris)
 - [3] [Importing and viewing the Iris dataset using pandas](https://www.angela1c.com/projects/iris_project/downloading-iris/) 
 - [4] [Pandas Tutorial](https://www.w3schools.com/python/pandas/default.asp)
 - [5] [An introduction to seaborn]( https://seaborn.pydata.org/tutorial/introduction)
 - [6] [Reading and Writing CSV Files in Python](https://realpython.com/python-csv/#reading-csv-files-with-pandas)
 - [7] [Pandas replace() – Replace Values in Pandas Dataframe](https://datagy.io/pandas-replace-values/)
 - [8] [How to Use Python to Write a Text File (.txt)](https://datagy.io/python-write-text-file/)         
 - [9] [Python | Pandas Dataframe/Series.head() method]( https://www.geeksforgeeks.org/python-pandas-dataframe-series-head-method/)
 - [10] [Exploratory Data Analysis on Iris Dataset](https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/)         
 - [11] [How to list unique values in a Pandas DataFrame?](https://www.projectpro.io/recipes/list-unique-values-in-pandas-dataframe) 
 - [12] [How to use .format in python to print out the data shape](https://stackoverflow.com/questions/58008120/how-to-use-format-in-python-to-print-out-the-data-shape) 
 - [13] [Pandas Join DataFrames on Columns](https://sparkbyexamples.com/pandas/pandas-join-dataframes-on-columns/) 
 - [14] [pandas.DataFrame.dtypes](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dtypes.html)
 - [15] [Pandas DataFrame: describe() function](https://www.w3resource.com/pandas/dataframe/dataframe-describe.php)
 - [16] [How to Generate a Data Summary in Python](https://learnpython.com/blog/how-to-summarize-data-in-python/)
 - [17] [Pandas DataFrame agg() Method](https://www.w3schools.com/python/pandas/ref_df_agg.asp)
 - [18] [How does pandas calculate quartiles?](https://stackoverflow.com/questions/55009203/how-does-pandas-calculate-quartiles)
 - [19] [Iris Dataset-Univariate, Bivariate & Multivariate](https://www.kaggle.com/code/amrut11/iris-dataset-univariate-bivariate-multivariate)
https://www.kaggle.com/code/amrut11/iris-dataset-univariate-bivariate-multivariate
 - [20] [How to Make a Beautiful Donut Chart and Nested Donut Chart in Matplotlib](https://plainenglish.io/blog/how-to-make-a-beautiful-donut-chart-and-nested-donut-chart-in-matplotlib-92040c8bbeea)
 - [21] [Pandas Get Unique Values in Column](https://sparkbyexamples.com/pandas/pandas-find-unique-values-from-columns/)
 - [22] [Pie charts]( https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html)
 - [23] [Seaborn Styles](https://www.educba.com/seaborn-styles/)
 - [24] [Make Better Bar Charts in Python using Pandas Plot](https://www.shanelynn.ie/bar-plots-in-python-using-pandas-dataframes/)
 - [25] [Rotate Axis Labels in Matplotlib]( https://stackabuse.com/rotate-axis-labels-in-matplotlib/)
 - [26] [Best fit to a histogramplot Iris](https://stackoverflow.com/questions/67300148/best-fit-to-a-histogramplot-iris)
 - [27] [Matplotlib.axes.Axes.set_xlabel() in Python](https://www.geeksforgeeks.org/matplotlib-axes-axes-set_xlabel-in-python/)
 - [28] [How to Adjust Spacing Between Matplotlib Subplots](https://www.statology.org/matplotlib-subplot-spacing/)
 - [29] [Exploratory Data Analysis of IRIS Data Set Using Python](https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d)
 - [30] [Violin Plots 101: Visualizing Distribution and Probability Density](https://mode.com/blog/violin-plot-examples/)
 - [31] [Exploratory Data Analysis : Iris Dataset](https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-4df6f045cda)
 - [32] [Data Visualization](https://deepnote.com/@econdesousa/ViolinPlotvsBoxPlot-aadf0c53-53b4-4221-89b9-4388c54c68bd)    
 - [33] [Seaborn Color Palettes](https://www.practicalpythonfordatascience.com/ap_seaborn_palette)    
 - [34] [Tutorial - Python SUBPLOTS](https://www.kaggle.com/code/asimislam/tutorial-python-subplots) 
 - [35] [How to change size of axis labels and values in seaborn pairsplot](https://stackoverflow.com/questions/45204552/how-to-change-size-of-axis-labels-and-values-in-seaborn-pairsplot)
 - [36] [matplotlib and seaborn heatmap renders differently in Jupyter to savefig (labels cut off)](https://stackoverflow.com/questions/51568083/matplotlib-and-seaborn-heatmap-renders-differently-in-jupyter-to-savefig-labels)
 - [37] [Auto adjust font size in seaborn heatmap](https://stackoverflow.com/questions/33104322/auto-adjust-font-size-in-seaborn-heatmap)    
 - [38] [Get Started With Colormaps (Cmap) in Python for Data Visualization Using Matplotlib (Updated 2023)](https://www.analyticsvidhya.com/blog/2020/09/colormaps-matplotlib/)
 - [39] [How do you add padding between the x-axis tick marks (not tick labels) and the x-axis in Matplotlib and Seaborn](https://stackoverflow.com/questions/66226320/how-do-you-add-padding-between-the-x-axis-tick-marks-not-tick-labels-and-the-x)
</p>
</details>

<details>
  <summary>Figure</summary>
           <p>
            
 - [Fig.1] [Iris Dataset Project from UCI Machine Learning Repository](https://machinelearninghd.com/iris-dataset-uci-machine-learning-repository-project/)
 - [Fig.2] [Machine Learning 101](https://www.bogotobogo.com/python/scikit-learn/scikit_machine_learning_features_extraction.php)
 - [Fig.3] [Violin Plots: A Box Plot-Density Trace Synergism.](http://www.sci.utah.edu/~kpotter/Library/Papers/hintze:1998:VPDT/index.html)
 
 </p>
</details>

<details>
    <summary>Other Sources consulted </summary>
           <p>
            
 - [How to add images to README.md on GitHub?](https://stackoverflow.com/questions/14494747/how-to-add-images-to-readme-md-on-github)
 - [How to customize Matplotlib plot titles color, position and fonts?](https://www.dataforeverybody.com/matplotlib-title-size-position-color/)
 - [Adding a main title to subplots in Matplotlib](https://www.skytowner.com/explore/adding_a_main_title_to_subplots_in_matplotlib)
 - [Plt.show shows full graph but savefig is cropping the image](https://stackoverflow.com/questions/37427362/plt-show-shows-full-graph-but-savefig-is-cropping-the-image)
 - [Seaborn Tutorial ](https://www.kaggle.com/code/saurav9786/seaborn-tutorial)
 - [How to Change Font Size in Seaborn Plots (With Examples)](https://www.statology.org/seaborn-font-size/)
 - [Matplotlib.pyplot.tight_layout() in Python](https://www.geeksforgeeks.org/matplotlib-pyplot-tight_layout-in-python/)
 - [List of named colors](https://matplotlib.org/stable/gallery/color/named_colors.html) 
 - [Choosing color palettes](https://seaborn.pydata.org/tutorial/color_palettes.html)  
 - [How to remove or hide X-axis labels from a Seaborn / Matplotlib plot?](https://www.tutorialspoint.com/how-to-remove-or-hide-x-axis-labels-from-a-seaborn-matplotlib-plot)             
 - [Kernel density estimation](https://en.wikipedia.org/wiki/Kernel_density_estimation)
 - [Exploring Classifiers with Python Scikit-learn — Iris Dataset](https://towardsdatascience.com/exploring-classifiers-with-python-scikit-learn-iris-dataset-2bcb490d2e1b)
 - [Exploratory Data Analysis: Uni-variate analysis of Iris Data set](https://medium.com/analytics-vidhya/exploratory-data-analysis-uni-variate-analysis-of-iris-data-set-690c87a5cd40)    
            
</p>
</details>
 
