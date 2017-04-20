

```python
# 1. Create a list named my_list in python 
my_list = [45.4, 44.2, 36.8, 35.1, 39.0, 60.0, 47.4, 41.1, 45.8, 35.6]
print (my_list)
```

    [45.4, 44.2, 36.8, 35.1, 39.0, 60.0, 47.4, 41.1, 45.8, 35.6]
    


```python
#a. Print the 5th element in the list
my_list[4]
```




    39.0




```python
#b. Append 55.2 to my_list
my_list.append(55.2)
print (my_list)
```

    [45.4, 44.2, 36.8, 35.1, 39.0, 60.0, 47.4, 41.1, 45.8, 35.6, 55.2, 55.2]
    


```python
#c.Remove the 6th element in the list
my_list.remove(60.0)
print (my_list)
```

    [45.4, 44.2, 36.8, 35.1, 39.0, 47.4, 41.1, 45.8, 35.6, 55.2, 55.2]
    


```python
#d. Iterate over the list to print data points greater than 45
data =[45.4, 44.2, 36.8, 35.1, 39.0, 60.0, 47.4, 41.1, 45.8, 35.6]
print(data)
for value in data:
    if value > 45:
        print(value)
```

    [45.4, 44.2, 36.8, 35.1, 39.0, 60.0, 47.4, 41.1, 45.8, 35.6]
    45.4
    60.0
    47.4
    45.8
    


```python
#a. Import the numpy library using the following command – import numpy
import numpy as np
x = np.array([45.4, 44.2, 36.8, 35.1, 39.0, 60.0, 47.4, 41.1, 45.8, 35.6])
print(x)
```

    [ 45.4  44.2  36.8  35.1  39.   60.   47.4  41.1  45.8  35.6]
    


```python
#c. Compute the mean and standard deviation using numpy.mean() and numpy.std() of the above array
numpy.mean(x)
```




    43.040000000000006




```python
#c. Compute the mean and standard deviation using numpy.mean() and numpy.std() of the above array
x = np.array([45.4, 44.2, 36.8, 35.1, 39.0, 60.0, 47.4, 41.1, 45.8, 35.6])
numpy.std(x)
```




    7.0611897014596625




```python
#d. Use logical referencing to get only those values that are less than 45
data =[45.4, 44.2, 36.8, 35.1, 39.0, 60.0, 47.4, 41.1, 45.8, 35.6]
print(data)
for value in data:
    if value < 45:
        print(value)
```

    [45.4, 44.2, 36.8, 35.1, 39.0, 60.0, 47.4, 41.1, 45.8, 35.6]
    44.2
    36.8
    35.1
    39.0
    41.1
    35.6
    


```python
#e. Compute the max and min of the array using numpy.max() and numpy.min()
numpy.max(data)
```




    60.0




```python
#e. Compute the max and min of the array using numpy.max() and numpy.min()
numpy.min(data)
```




    35.100000000000001




```python
#a. Import the pandas library – import pandas
#b. Read the IRIS dataset into iris using pandas.read_csv(). Data file – 
#c. Using iris.head(), display the head of the dataset
import pandas as pd
iris = pd.read_csv("C:/Users/Deer/Downloads/Iris.csv")
print(iris.head())
```

       Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm      Species
    0   1            5.1           3.5            1.4           0.2  Iris-setosa
    1   2            4.9           3.0            1.4           0.2  Iris-setosa
    2   3            4.7           3.2            1.3           0.2  Iris-setosa
    3   4            4.6           3.1            1.5           0.2  Iris-setosa
    4   5            5.0           3.6            1.4           0.2  Iris-setosa
    


```python
#d. Use DataFrame.drop() to drop the id column
import pandas as pd
iris = pd.read_csv("C:/Users/Deer/Downloads/Iris.csv")
x3 = iris.drop(iris.columns[0], axis=1)
print(x3.head())
```

       SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm      Species
    0            5.1           3.5            1.4           0.2  Iris-setosa
    1            4.9           3.0            1.4           0.2  Iris-setosa
    2            4.7           3.2            1.3           0.2  Iris-setosa
    3            4.6           3.1            1.5           0.2  Iris-setosa
    4            5.0           3.6            1.4           0.2  Iris-setosa
    


```python
#e.	Subset dataframe to create a new data frame that includes only the measurements for the setosa species
iris = pd.read_csv("C:/Users/Deer/Downloads/Iris.csv")
x4 = iris.query('Species == "Iris-setosa" ')
print(x4.head())
print(x4.tail())
```

       Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm      Species
    0   1            5.1           3.5            1.4           0.2  Iris-setosa
    1   2            4.9           3.0            1.4           0.2  Iris-setosa
    2   3            4.7           3.2            1.3           0.2  Iris-setosa
    3   4            4.6           3.1            1.5           0.2  Iris-setosa
    4   5            5.0           3.6            1.4           0.2  Iris-setosa
        Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm      Species
    45  46            4.8           3.0            1.4           0.3  Iris-setosa
    46  47            5.1           3.8            1.6           0.2  Iris-setosa
    47  48            4.6           3.2            1.4           0.2  Iris-setosa
    48  49            5.3           3.7            1.5           0.2  Iris-setosa
    49  50            5.0           3.3            1.4           0.2  Iris-setosa
    


```python
#f.	Use DataFrame.describe() to get the summary statistics
iris.describe() 
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Id</th>
      <th>SepalLengthCm</th>
      <th>SepalWidthCm</th>
      <th>PetalLengthCm</th>
      <th>PetalWidthCm</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>150.000000</td>
      <td>150.000000</td>
      <td>150.000000</td>
      <td>150.000000</td>
      <td>150.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>75.500000</td>
      <td>5.843333</td>
      <td>3.054000</td>
      <td>3.758667</td>
      <td>1.198667</td>
    </tr>
    <tr>
      <th>std</th>
      <td>43.445368</td>
      <td>0.828066</td>
      <td>0.433594</td>
      <td>1.764420</td>
      <td>0.763161</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>4.300000</td>
      <td>2.000000</td>
      <td>1.000000</td>
      <td>0.100000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>38.250000</td>
      <td>5.100000</td>
      <td>2.800000</td>
      <td>1.600000</td>
      <td>0.300000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>75.500000</td>
      <td>5.800000</td>
      <td>3.000000</td>
      <td>4.350000</td>
      <td>1.300000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>112.750000</td>
      <td>6.400000</td>
      <td>3.300000</td>
      <td>5.100000</td>
      <td>1.800000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>150.000000</td>
      <td>7.900000</td>
      <td>4.400000</td>
      <td>6.900000</td>
      <td>2.500000</td>
    </tr>
  </tbody>
</table>
</div>




```python
#g.Use DataFrame.groupby() to create grouped data frames by Species and compute summary statistics using DataFrame.describe()
x5 = iris.groupby("Species") 
x5.describe()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Id</th>
      <th>PetalLengthCm</th>
      <th>PetalWidthCm</th>
      <th>SepalLengthCm</th>
      <th>SepalWidthCm</th>
    </tr>
    <tr>
      <th>Species</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="8" valign="top">Iris-setosa</th>
      <th>count</th>
      <td>50.00000</td>
      <td>50.000000</td>
      <td>50.000000</td>
      <td>50.000000</td>
      <td>50.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>25.50000</td>
      <td>1.464000</td>
      <td>0.244000</td>
      <td>5.006000</td>
      <td>3.418000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>14.57738</td>
      <td>0.173511</td>
      <td>0.107210</td>
      <td>0.352490</td>
      <td>0.381024</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.00000</td>
      <td>1.000000</td>
      <td>0.100000</td>
      <td>4.300000</td>
      <td>2.300000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>13.25000</td>
      <td>1.400000</td>
      <td>0.200000</td>
      <td>4.800000</td>
      <td>3.125000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>25.50000</td>
      <td>1.500000</td>
      <td>0.200000</td>
      <td>5.000000</td>
      <td>3.400000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>37.75000</td>
      <td>1.575000</td>
      <td>0.300000</td>
      <td>5.200000</td>
      <td>3.675000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>50.00000</td>
      <td>1.900000</td>
      <td>0.600000</td>
      <td>5.800000</td>
      <td>4.400000</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">Iris-versicolor</th>
      <th>count</th>
      <td>50.00000</td>
      <td>50.000000</td>
      <td>50.000000</td>
      <td>50.000000</td>
      <td>50.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>75.50000</td>
      <td>4.260000</td>
      <td>1.326000</td>
      <td>5.936000</td>
      <td>2.770000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>14.57738</td>
      <td>0.469911</td>
      <td>0.197753</td>
      <td>0.516171</td>
      <td>0.313798</td>
    </tr>
    <tr>
      <th>min</th>
      <td>51.00000</td>
      <td>3.000000</td>
      <td>1.000000</td>
      <td>4.900000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>63.25000</td>
      <td>4.000000</td>
      <td>1.200000</td>
      <td>5.600000</td>
      <td>2.525000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>75.50000</td>
      <td>4.350000</td>
      <td>1.300000</td>
      <td>5.900000</td>
      <td>2.800000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>87.75000</td>
      <td>4.600000</td>
      <td>1.500000</td>
      <td>6.300000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>100.00000</td>
      <td>5.100000</td>
      <td>1.800000</td>
      <td>7.000000</td>
      <td>3.400000</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">Iris-virginica</th>
      <th>count</th>
      <td>50.00000</td>
      <td>50.000000</td>
      <td>50.000000</td>
      <td>50.000000</td>
      <td>50.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>125.50000</td>
      <td>5.552000</td>
      <td>2.026000</td>
      <td>6.588000</td>
      <td>2.974000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>14.57738</td>
      <td>0.551895</td>
      <td>0.274650</td>
      <td>0.635880</td>
      <td>0.322497</td>
    </tr>
    <tr>
      <th>min</th>
      <td>101.00000</td>
      <td>4.500000</td>
      <td>1.400000</td>
      <td>4.900000</td>
      <td>2.200000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>113.25000</td>
      <td>5.100000</td>
      <td>1.800000</td>
      <td>6.225000</td>
      <td>2.800000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>125.50000</td>
      <td>5.550000</td>
      <td>2.000000</td>
      <td>6.500000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>137.75000</td>
      <td>5.875000</td>
      <td>2.300000</td>
      <td>6.900000</td>
      <td>3.175000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>150.00000</td>
      <td>6.900000</td>
      <td>2.500000</td>
      <td>7.900000</td>
      <td>3.800000</td>
    </tr>
  </tbody>
</table>
</div>




```python
#h.Use DataFrame.boxplot() to plot boxplots by Species
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
iris = pd.read_csv("C:/Users/Deer/Downloads/Iris.csv")
x5 = iris.groupby("Species")
x5.boxplot(by="Species") 
```

    C:\Users\Deer\Anaconda3\lib\site-packages\pandas\core\frame.py:5749: UserWarning: To output multiple subplots, the figure containing the passed axes is being cleared
      return_type=return_type, **kwds)
    




    Iris-setosa        [[Axes(0.1,0.679412;0.363636x0.220588), Axes(0...
    Iris-versicolor    [[Axes(0.1,0.679412;0.363636x0.220588), Axes(0...
    Iris-virginica     [[Axes(0.1,0.679412;0.363636x0.220588), Axes(0...
    dtype: object




```python
#i. Plot a scatter matrix plot using the seaborn library. Use the following to load and plot 
#i. Import seaborn
#ii. Seaborn.pairplot(dataframe,by=’column_name’)
import seaborn as sns
sns.pairplot(iris,hue='Species')
```




    <seaborn.axisgrid.PairGrid at 0xb3fd8d0>


