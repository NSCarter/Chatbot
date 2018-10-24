import numpy as np

file = 'General Names.csv'

keywords = ['park']
outputInfo = []

name = np.genfromtxt(file, delimiter=',', names=True, dtype=None)   #Loads the contents of the csv file, seperates it by comma and converts it to string

#Lists of keywords to be recognised
drinkingKey = ['drinking', 'club', 'pub', 'drinks', 'drink',' clubs', 'pubs', 'nightclub', 'nightclubs']


clothingKey = ['clothing', 'clothes', 'shop', 'shops', 'shopping']
fitnessKey = ['fitness', 'gym', 'sport']
activitiesKey = ['activity', 'activities', 'museum']
parksKey = ['park', 'reserve']

#print(str(name['Drinking'][1]))                                             #Prints the column with a certain header name

'''Keywords entered in a list, information is found and returned in a list'''
def findInfo(keywords):

    def fixEntry(entry):
        entry = entry.translate({ord(c): None for c in '\'[]'})
        entry = entry.strip('\n')
        if entry[0] == 'b' and entry not in ['belgrade theatre', 'brandon marsh nature reserve']:
            entry = entry[1:]
        return entry
    
    #Look at each keyword and see if they belong to a catergory
    #If a category has been found, check to see if the results can be more specific to the keyword
    for word in keywords:  #For each keyword in the users input
        if word in drinkingKey:    #If the word is in one of the keys
            lis = list((str(name['drinking'])).split(' b')) #Create a list all all the information on that topic
            for entry in lis:   ##Check to see if the information can be more specific based on the keyword#Check to see if the information can be more specific based on the keyword
                if word in entry:
                    entry = fixEntry(entry)
                    outputInfo.append(entry)
        elif word in activitiesKey:
            lis = list((str(name['activites'])).split(' b'))
            for entry in lis:
                if word in entry:
                    entry = fixEntry(entry)
                    outputInfo.append(entry)

        elif word in clothingKey:
            lis = list((str(name['clothing'])).split(' b'))
            for entry in lis:
                if word in entry:
                    entry = fixEntry(entry)
                    outputInfo.append(entry)
        elif word in fitnessKey:
            lis = list((str(name['fitness'])).split(' b'))
            for entry in lis:
                if word in entry:
                    entry = fixEntry(entry)
                    outputInfo.append(entry)
        elif word in parksKey:
            lis = (str(name['parks'])).split(' b')
            for entry in lis:
                if word in entry:
                    entry = fixEntry(entry)
                    outputInfo.append(entry)
        else:
            print ('No information found')

    return outputInfo



print(findInfo(keywords))
