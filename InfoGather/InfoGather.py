import numpy as np

file = 'General Names.csv'

keywords = ['museum']

name = np.genfromtxt(file, delimiter=',', names=True, dtype=None)   #Loads the contents of the csv file, seperates it by comma and converts it to string

#Lists of keywords to be recognised
drinkingKey = ['drinking', 'club', 'pub', 'drinks', 'drink',' clubs', 'pubs', 'nightclub', 'nightclubs']
clothingKey = ['clothing', 'clothes', 'shop', 'shops', 'shopping']
fitnessKey = ['fitness', 'gym', 'sport']
activitiesKey = ['activity', 'activities', 'museum']

#print(str(name['Drinking'][1]))                                             #Prints the column with a certain header name

#Look at each keyword and see if they belong to a catergory
#If a category has been found, check to see if the results can be more specific to the keyword
for i in keywords:  
    if i in drinkingKey:
        lis = list((str(name['Activites'])).split(' b'))
    elif i in activitiesKey:
        lis = list((str(name['Activites'])).split(' b'))

        for c in lis:
            if i in c:
                print (c)
