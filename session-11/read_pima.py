from pandas import read_csv
dataset = read_csv('diabetes.csv', header=None)
print(dataset.describe())

