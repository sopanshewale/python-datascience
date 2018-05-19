#!/usr/local/Cellar/python3/3.6.3/bin/python3
from matplotlib import pyplot as plt
from sklearn.datasets import  load_iris
import numpy as np 
import pandas as pd

loaded=load_iris()
features=loaded["data"]
feature_names = loaded["feature_names"]
labels=loaded["target"]


print ("Features: ---->")
print (features) 
print ("Feature Names: ---->")
print (feature_names)
print ("Labels: ---->")
print (labels)



features=pd.DataFrame(features)

print (features)

labels=pd.DataFrame(labels)

print (labels) 

features[4]=labels

for i,color in zip(range(3),"rbg"):
     plt.scatter(features[features[4]==i][0],features[features[4]==i][1],c=color,marker="o")  
 
#plt.show()
plt.savefig('iris.png')

