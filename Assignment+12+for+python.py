
# coding: utf-8

# In[2]:

# 1. Create a list named my_list in python 
my_list = [45.4, 44.2, 36.8, 35.1, 39.0, 60.0, 47.4, 41.1, 45.8, 35.6]
print (my_list)


# In[16]:

#a. Print the 5th element in the list
my_list[4]


# In[5]:

#b. Append 55.2 to my_list
my_list.append(55.2)
print (my_list)


# In[6]:

#c.Remove the 6th element in the list
my_list.remove(60.0)
print (my_list)


# In[10]:

#d. Iterate over the list to print data points greater than 45
data =[45.4, 44.2, 36.8, 35.1, 39.0, 60.0, 47.4, 41.1, 45.8, 35.6]
print(data)
for value in data:
    if value > 45:
        print(value)


# In[24]:

#a. Import the numpy library using the following command – import numpy
import numpy as np
x = np.array([45.4, 44.2, 36.8, 35.1, 39.0, 60.0, 47.4, 41.1, 45.8, 35.6])
print(x)


# In[27]:

#c. Compute the mean and standard deviation using numpy.mean() and numpy.std() of the above array
numpy.mean(x)


# In[35]:

#c. Compute the mean and standard deviation using numpy.mean() and numpy.std() of the above array
x = np.array([45.4, 44.2, 36.8, 35.1, 39.0, 60.0, 47.4, 41.1, 45.8, 35.6])
numpy.std(x)


# In[36]:

#d. Use logical referencing to get only those values that are less than 45
data =[45.4, 44.2, 36.8, 35.1, 39.0, 60.0, 47.4, 41.1, 45.8, 35.6]
print(data)
for value in data:
    if value < 45:
        print(value)


# In[37]:

#e. Compute the max and min of the array using numpy.max() and numpy.min()
numpy.max(data)


# In[38]:

#e. Compute the max and min of the array using numpy.max() and numpy.min()
numpy.min(data)


# In[5]:

#a. Import the pandas library – import pandas
#b. Read the IRIS dataset into iris using pandas.read_csv(). Data file – 
#c. Using iris.head(), display the head of the dataset
import pandas as pd
iris = pd.read_csv("C:/Users/Deer/Downloads/Iris.csv")
print(iris.head())


# In[13]:

#d. Use DataFrame.drop() to drop the id column
import pandas as pd
iris = pd.read_csv("C:/Users/Deer/Downloads/Iris.csv")
x3 = iris.drop(iris.columns[0], axis=1)
print(x3.head())


# In[20]:

#e.	Subset dataframe to create a new data frame that includes only the measurements for the setosa species
iris = pd.read_csv("C:/Users/Deer/Downloads/Iris.csv")
x4 = iris.query('Species == "Iris-setosa" ')
print(x4.head())
print(x4.tail())


# In[21]:

#f.	Use DataFrame.describe() to get the summary statistics
iris.describe() 


# In[23]:

#g.Use DataFrame.groupby() to create grouped data frames by Species and compute summary statistics using DataFrame.describe()
x5 = iris.groupby("Species") 
x5.describe()


# In[10]:

#h.Use DataFrame.boxplot() to plot boxplots by Species
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
iris = pd.read_csv("C:/Users/Deer/Downloads/Iris.csv")
x5 = iris.groupby("Species")
x5.boxplot(by="Species") 


# In[6]:

#i. Plot a scatter matrix plot using the seaborn library. Use the following to load and plot 
#i. Import seaborn
#ii. Seaborn.pairplot(dataframe,by=’column_name’)
import seaborn as sns
sns.pairplot(iris,hue='Species')

