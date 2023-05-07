
# import needed libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
import seaborn as sns

# import data from a csv file using pandas 
df = pd.read_csv('iris_dataset.csv')

# replace the 3 spieces with a more friendly name 
df["Species"].replace(to_replace="Iris-setosa", value="Setosa", inplace=True)
df["Species"].replace(to_replace="Iris-versicolor", value="Versicolor", inplace=True)
df["Species"].replace(to_replace="Iris-virginica", value="Virginica", inplace=True)

# create the text file and write on them 
with open ('iris_analysis.txt', 'w') as f:
    # print an introduction of the text file 
    f.write("Project for the Subject Programming and Scripting \n \n")
    f.write("Author: Cecilia Pastore \n ")
    f.write("iris_analysis.txt \n \n")
    # checking the first 5 line of the dataset to see if the format fit
    f.write("==== First 5 lines of the dataset ==== \n \n")
    f.write(str(df.head())+'\n \n')
    # print unique value on the the species colume to check no duplicate and that the replace has been done correctly 
    f.write("==== Print unique value of species ==== \n \n")
    unique_species = pd.unique(df['Species'])
    f.write("Species\n \n")
    for species in unique_species:
        f.write(species)
        f.write("\n")
    f.write("\n")
    # checking missing value
    f.write("==== Checking missing value ==== \n \n")
    f.write(str(df.isnull().sum())+'\n \n')
    # shape of the datased
    f.write("==== Shape of the dataset ==== \n \n")
    f.write("Number of rows: {}\n".format(df.shape[0]))
    f.write("Number of columns: {}\n".format(df.shape[1]))
    f.write("Size: {}\n".format(df.size))
    f.write("Columns: {}\n\n".format(", ".join(df.columns)))
    f.write(str(df.value_counts("Species"))+'\n\n')
    # get the data type 
    f.write("==== Data type ==== \n \n")
    f.write("Attribute \t \t \t \t Type \n \n")
    f.write(str(df.dtypes)+'\n\n')
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
plt.pie(group_count, labels=labels, autopct='%1.0f%%', 
        textprops={'fontsize': 14, 'fontweight': 'bold'},
        wedgeprops={'linewidth': 2, 'edgecolor': 'white', 'alpha':0.7})
# create a white cirle to have the donut effect 
centre_circle= plt.Circle((0,0),0.65,color='white', fc='white',linewidth=1.00)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.axis('equal')
# print a title
plt.title('Distribution of Species', color='Red', fontweight='bold', fontsize=20)
# save the plot as immage 
plt.savefig("Plot1_PieOfDistribution.png")

# Create a bar plot with the mean of each categories per species [4]
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
plt.savefig('Plot2_AverageBar')

# make the 'species' column categorical to fix the order
df['Species'] = pd.Categorical(df['Species'])
# create a 2x2 subplot
fig, axs = plt.subplots(2, 2, figsize=(12, 6))
# initialize a counter for the subplot index
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
# adjust the spacing between the subplots and set the figure title
fig.subplots_adjust(hspace=0.4, top=0.85, right=0.8)
fig.suptitle('Distribution of Iris Flower Features', fontsize=16, color='red', fontweight='bold')
# adjust the layout and save the figure  
plt.tight_layout()
plt.savefig("Plot3_Subplot_Feature.png")

# Create a supbplot with 4 scatterpoint comparing 2 features each 
fig = plt.figure(figsize=(14,7))
# Set the style of the plot to "darkgrid"
sns.set_style("darkgrid")
# Adjust the space between subplots and the top margin of the figure
fig.subplots_adjust(hspace=0.4, top=0.85)
# Add a  title to the entire figure
plt.suptitle("Comparison between various Species", fontsize=18, color='red', fontweight='bold')

# Create the first scatter plot comparing Sepal Length and Sepal Width
plt.subplot(221)
plt.title("Sepal Length and Width", fontsize=16, fontweight='bold')
sns.scatterplot(x=df['SepalLenght(cm)'], y=df['SepalWidth(cm)'], hue=df['Species'], s=80, alpha=0.8, palette="Dark2")

# Create the second scatter plot comparing Petal Length and Petal Width
plt.subplot(222)
plt.title("Petal Length and Width", fontsize=16, fontweight='bold')
sns.scatterplot(x=df['PetalLenght(cm)'], y=df['PetalWidth(cm)'], hue=df['Species'], s=80, alpha=0.8, palette="Dark2", legend=False)

# Create the second scatter plot comparing Petal Length and Sepal Width
plt.subplot(223)
plt.title("Petal Length and Sepal Width", fontsize=16, fontweight='bold')
sns.scatterplot(x=df['PetalLenght(cm)'], y=df['SepalLenght(cm)'], hue=df['Species'], s=80, alpha=0.8, palette="Dark2", legend=False)

# Create the second scatter plot comparing comparing Petal Width and Sepal Length
plt.subplot(224)
plt.title("Petal Widht and Sepal Lenght", fontsize=16, fontweight='bold')
sns.scatterplot(x=df['PetalWidth(cm)'], y=df['SepalLenght(cm)'], hue=df['Species'], s=80, alpha=0.8, palette="Dark2", legend=False)

# Adjust the layout and save the figure 
plt.tight_layout()
plt.savefig("Plot4_Subplot_scatterpoint.png")

# Set the context for the plot, adjusting the size of the labels and fonts
sns.set_context("paper", rc={"axes.labelsize":20})
sns.set_context("talk", font_scale=1.4)
# Create a pairplot of the dataset
sns.pairplot(df,hue='Species', height=4, palette = 'colorblind')
# Add a title to the entire figure, adjust the top margin and save the figure 
plt.suptitle("Scatterplots of all-paired attributes", fontsize=20, fontweight='bold', color = 'red')
plt.subplots_adjust(top=0.95)
plt.savefig("Plot5_pairplot.png")