
# import needed libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
import seaborn as sns
from scipy.stats import norm

# import data from a csv file using pandas 
df = pd.read_csv('iris_dataset.csv')

# change the colums name in a nicer format 
columns = ['SepalLenght(cm)', 'SepalWidth(cm)', 'PetalLenght(cm)', 'PetalWidth(cm)', 'Species']
df.columns = columns

# replace the 3 spieces with a more friendly name 
df["Species"].replace(to_replace="Iris-setosa", value="Setosa", inplace=True)
df["Species"].replace(to_replace="Iris-versicolor", value="Versicolor", inplace=True)
df["Species"].replace(to_replace="Iris-virginica", value="Virginica", inplace=True)

# create the tile and write on them 
with open ('iris_analysis.txt', 'w') as f:
    f.write("Project for the Subject Programming and Scripting \n \n")
    f.write("Author: Cecilia Pastore \n ")
    f.write("iris_analysis.txt \n \n")
    # check the first 5 line of the dataset to see if the format fit
    f.write("==== First 5 line of the dataset ==== \n \n")
    f.write(str(df.head())+'\n \n')
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
    # get an user more friendly view of the statistics 
    # for loop to print for each species the varaible mean, median, std, min, max 
    for column in df.columns[:-1]:
        f.write(f"==== {column} Statistics ====\n\n")
        f.write(f"{df.groupby('Species')[column].agg(['mean', 'median', 'std', 'min', 'max'])}\n\n")
    # get quartile per species 
    f.write("==== Quartiles per species ==== \n \n")
    f.write(str(df.groupby('Species').quantile([0.25, 0.50, 0.75]))+'\n\n')

# create a pie chart to show the distribution of species - source [1], [2], [3]
# get the count of each species
group_count= df['Species'].value_counts()
# define the labels of the pie chart
labels= df['Species'].unique()
# set the parameters of the pie chart
plt.pie(group_count, labels=labels, radius=1.3, autopct='%1.0f%%', startangle=90, counterclock=False,
        textprops={'fontsize': 14, 'fontweight': 'bold'},
        wedgeprops={'linewidth': 2, 'edgecolor': 'white', 'alpha':0.7})
# create a white cirle to have the donut effect 
centre_circle= plt.Circle((0,0),0.65,color='white', fc='white',linewidth=1.00)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.axis('equal')
plt.title('Distribution of Species', color='Red', fontweight='bold', fontsize=20)
plt.savefig("Plot1_PieOfDistribution.png")

# Create a bar plot with the average of each categories per species [4]

# Compute the average of each feature for each class
class_averages = df.groupby('Species').mean()

# select a seaborn style 
sns.set_style("dark")

# Create the bar chart
class_averages.plot(kind='bar', alpha=0.7)
plt. title('Iris Feature Averages by Species', fontweight = 'bold', fontsize = 20)
plt. xlabel('Species', fontweight = 'bold', fontsize = 14)
plt. ylabel('Average', fontweight = 'bold', fontsize = 14)
# rotate the x values [5]
plt.xticks(rotation=0)
plt.savefig('Plot1_AverageBar')
plt.show()

#plt.bar(df.feature_names, average)
#plt.title("Bar Chart Setosa Averages")
#plt.ylabel("Average (in cm)")
#plt.show()


            

'''# Create a barplot of 

fig, axs= plt.subplots(nrows=1, ncols=2, figsize=(12,6))

plt.show()

# Create a subplots of histograms with each speciel in different color and a KDE curve 

df['Species'] = pd.Categorical(df['Species'], categories=['Setosa', 'Versicolor', 'Virginica'])

fig, axs = plt.subplots(2, 2, figsize=(12, 6))
for col, ax in zip(df.columns[:4], axs.flat):
     sns.histplot(data=df, x=col, kde=True, hue='Species', common_norm=False, legend=ax==axs[0,0], ax=ax)
     ax.set_title(col.capitalize())
     ax.set_xlabel(None)
     ax.set_ylabel('Count')

fig.subplots_adjust(hspace=0.4, top=0.85)
fig.suptitle('Distribution of Iris Flower Features', fontsize=16, color='red', fontweight='bold')

plt.tight_layout()
plt.savefig("Subplot.png")
#plt.show()

## Plot Boxplots 

plt.figure(figsize=(10,8))
sns.set_style("whitegrid")
plt.title('Comparing different species based on their sepal length and width', fontsize=16, color='red')
plt.xlabel('Sepal Length (cm)', fontsize=14, color='blue')
plt.ylabel('Sepal Width (cm)', fontsize=14, color='blue')
sns.scatterplot(df['SepalLenght(cm)'], df['SepalWidth(cm)'], hue=df['Species'], s=80, alpha=0.8, palette="Dark2")
plt.legend(loc='upper right', fontsize=12)
plt.savefig("Plot.png")
#plt.show()'''

'''plt.figure(figsize=(8,6))
plt.title('Comparing different species based on their sepal length and width')    
sns.scatterplot(df['SepalLenght(cm)'],df['SepalWidth(cm)'],hue =df['Species'],s=50)
plt.show()'''   
