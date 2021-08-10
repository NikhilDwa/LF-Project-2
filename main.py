import csv
import numpy as np
import matplotlib.pyplot as plt


def reading_csv():
    try:
        with open('kc_house_data.csv', 'r') as file:
            reader = csv.reader(file, delimiter=',', quotechar='"')
            data = [row for row in reader]
        return np.asarray(data, dtype=None)
    except:
        print("No csv found")
        return
