import numpy as np

file = 'General Names.csv'

name = np.genfromtxt(file, delimiter=',', names=True, dtype=None)   #Loads the contents of the csv file, seperates it by comma and converts it to string

print(name['Drinking'])  
