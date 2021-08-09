import numpy as np 
import matplotlib.pyplot as plt

data_array = np.loadtxt("kc_house_data.csv", delimiter = ",", dtype='object')

print(data_array)