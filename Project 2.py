import numpy as np 
import matplotlib.pyplot as plt

data_array = np.loadtxt("kc_house_data.csv", delimiter = ",", dtype='object')

print(data_array)

print(data_array[0])

head = data_array[0:6,]

print(head)

for index, value in enumerate(data_array[0]):
    print(index, value)