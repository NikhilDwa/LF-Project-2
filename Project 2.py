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

"""### Fetching the new indexes"""

for index, value in enumerate( new_data_array[0] ):
    print(index, value)

"""### Data type conversion"""
print(new_data_array[1:, 5])

array = np.array([])
for i in new_data_array[1:, 5]: 
    array = np.append(array, i[1:-1])

print(array)

new_data_array[1:, 5] = array

"""### Checking for null values"""

np.all(np.isnan(new_data_array[1:, :].astype('float')))

print(new_data_array[0:1,0])

"""### Calculating the stastics for the feature **price**"""

all_price = new_data_array[1:,0]
all_price = all_price.astype('float64')

count_price = len(all_price)

all_price = all_price[all_price != 0] # remove all 0s from the array

mean_price = np.mean(all_price); std_price = np.std(all_price); min_price = min(all_price)
max_price = max(all_price); _25_price = np.percentile(all_price, 25); _50_price = np.percentile(all_price, 50)
_75_price = np.percentile(all_price, 75); lt_mean_price = np.count_nonzero(all_price < _50_price) # how many values less than mean
gte_mean_price = np.count_nonzero(all_price >= _50_price) #how many values greater than or equal to mean
iqr = _75_price - _25_price # inter-quartile range
rng = max_price - min_price # range of data


print(count_price,mean_price,std_price,min_price,max_price)
print(_25_price,_50_price,_75_price,lt_mean_price,gte_mean_price,iqr,rng)

"""



### Price data visual"""

x = [i for i in range(len(new_data_array[1:,0]))]

plt.title("county price")
plt.ylim(min_price , max_price )
plt.scatter(x=x, y=all_price,alpha=0.15)
plt.hlines(y=mean_price, xmin=0, xmax=len(new_data_array[1:,0]), colors='r')
plt.show()

#Outlier removal using percentile.

max_thresold = np.percentile(all_price, 99)
min_threshold = np.percentile(all_price, 1)

print(max_thresold, min_threshold)

all_price_no_outliers = []
for y in all_price.tolist():
    if y >= min_threshold and y <= max_thresold:
        all_price_no_outliers.append(y)

print("outlier percentage : ", (len(all_price)-len(all_price_no_outliers))/len(all_price) * 100)

count_price = np.count_nonzero(all_price_no_outliers)
mean_price = np.mean(all_price_no_outliers)
std_price = np.std(all_price_no_outliers)
min_price = min(all_price_no_outliers)
max_price = max(all_price_no_outliers)
_25_price = np.percentile(all_price_no_outliers, 25)
_50_price = np.percentile(all_price_no_outliers, 50)
_75_price = np.percentile(all_price_no_outliers, 75)
lt_mean_price = np.count_nonzero(all_price_no_outliers < _50_price) # how many values less than mean
gte_mean_price = np.count_nonzero(all_price_no_outliers >= _50_price) #how many values greater than or equal to mean
iqr = _75_price - _25_price # inter-quartile range
rng = max_price - min_price # range of data

print(count_price)
print(mean_price)
print(std_price)
print(min_price)
print(max_price)
print(_25_price)
print(_50_price)
print(_75_price)
print(lt_mean_price)
print(gte_mean_price)
print(iqr)

x = [i for i in range(len(all_price_no_outliers))]

plt.title("county price")
plt.ylim(min_price , max_price )
plt.scatter(x=x, y=all_price_no_outliers,alpha=0.15)
plt.hlines(y=mean_price, xmin=0, xmax=len(all_price_no_outliers), colors='r')
plt.show()

print(new_data_array[0], len(new_data_array[0]))