import numpy as np

file = 'General Names.csv'

names = np.loadtxt(file, delimiter=',', dtype=str)  #Loads the contents of the csv file, seperates it by comma and converts it to string

print(names)
