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

#Creating a dictionary with the above features as keys and the statistical calculations as values of the keys

stat = dict()
for i in new_data_array[0]:
    stat[i] = {'count':0, 'mean':0, 'std':0, 'min':0, 'max':0, '25%':0, '50%':0, '75%':0, 'bmean':0, 'amean':0, 'iqr':0, 'rng':0}


print(stat['bedrooms'])


print(stat.keys())

#Creating a dictionary with the above features as keys and assigning the data of the features as values

print(new_data_array[1:,0])

data = dict()
for i in range(len(new_data_array[0])):
    data[new_data_array[0][i]] = new_data_array[1:,i]
print(data['price'])

print(data)

#Doing the calculation and appending it to the stat dictionary accordingly

print(stat.keys())


for i in stat.keys():
    data[i] = data[i].astype('float64')
    
    stat[i]['count'] = np.count_nonzero(data[i])
    stat[i]['mean'] = '{0:.2f}'.format(np.mean(data[i]))
    stat[i]['std'] = '{0:.2f}'.format(np.std(data[i]))
    stat[i]['min'] = min(data[i])
    stat[i]['max'] = max(data[i])
    stat[i]['25%'] = np.percentile(data[i], 25)
    stat[i]['50%'] = np.percentile(data[i], 50)
    stat[i]['75%'] = np.percentile(data[i], 75)
    stat[i]['bmean'] = np.count_nonzero(data[i] < stat[i]['50%']) # how many values less than mean
    stat[i]['amean'] = np.count_nonzero(data[i] >= stat[i]['50%']) #how many values greater than or equal to mean
    stat[i]['iqr'] = stat[i]['75%'] - stat[i]['25%'] # inter-quartile range
    stat[i]['rng'] = stat[i]['max'] - stat[i]['min'] # range of data


print(stat['bedrooms'])

#Checking the frequency of unique values in the grade column

grade_data = new_data_array[1:,9]
print(grade_data[0:5])


(unique, counts) = np.unique(grade_data, return_counts=True)
frequencies = np.asarray((unique, counts)).T
print(frequencies)

grade_data = new_data_array[1:,9]
print(grade_data[0:5])

(unique, counts) = np.unique(grade_data, return_counts=True)
frequencies = np.asarray((unique, counts)).T
print(frequencies)

frequencies[:, 0].astype('int')

plt.bar(frequencies[:, 0].astype('int'), frequencies[:, 1].astype('int'))

#For bedrooms and bathrooms, we saw the minimum values to be 0. Since there are no homes with 0 bedrooms or bathrooms, we will remove the rows that contain such anamolies.

print(new_data_array.shape)

np.count_nonzero(new_data_array[1:, 1].astype('float')), np.count_nonzero(new_data_array[1:, 2].astype('float'))

data = new_data_array[1:, :]
data = data.astype('float')

data = np.delete(data, np.where(
    (data[:,1] == 0.0) | (data[:, 2] == 0.0)), axis=0)

np.count_nonzero(data[:, 1]), np.count_nonzero(data[:, 2])

(unique, counts) = np.unique(data[:,9].astype('int'), return_counts=True)
frequencies = np.asarray((unique, counts)).T
print(frequencies)

plt.bar(frequencies[:, 0], frequencies[:, 1])

#Creating an empty array to put the calculation in a tabular form.

new_array = np.empty((13,13), dtype='object')

new_array[1:, 0] = ['count', 'mean', 'std', 'min', 'max', '25%', '50%', '75%', 'bmean', 'amean', 'iqr', 'rng']

new_array[0, 1:] = ['price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade', 'sqft_above', 'sqft_basement']

for i in range(0,12):
    for j in range(0, 12):
    # print(i,j)
        new_array[i+1][j+1] = stat[new_array[0][j+1]][new_array[i+1][0]]

