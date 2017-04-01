from pandas import read_csv
import numpy
dataset = read_csv('diabetes.csv', header=None)
# mark zero values as missing or NaN

dataset[[1,2,3,4,5]] = dataset[[1,2,3,4,5]].replace(0, numpy.NaN)

# count the number of NaN values in each column
print(dataset.isnull().sum())
