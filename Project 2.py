import numpy as np 
import matplotlib.pyplot as plt

data_array = np.loadtxt("kc_house_data.csv", delimiter = ",", dtype='object')

print(data_array)

print(data_array[0])

head = data_array[0:6,]

print(head)

for index, value in enumerate(data_array[0]):
    print(index, value)
    
"""### Dropping irrelevant data points"""

new_data_array = np.delete(data_array, [0, 1, 14, 15, 16, 17, 18, 19, 20], axis=1)

"""### Column headings after dropping some of the column form the dataset."""

print(new_data_array[0])

