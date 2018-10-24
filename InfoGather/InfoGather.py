import numpy as np

file = 'General Names.csv'

#keywords = ['museum']   #Keywords found from the users input 
outputInfo = []

name = np.genfromtxt(file, delimiter=',', names=True, dtype=None)   #Loads the contents of the csv file, seperates it by comma and converts it to string, code from DataCamp - Importing Data in Python

#Lists of keywords to be recognised
drinkingKey = ['drinking', 'club', 'pub', 'drinks', 'drink',' clubs', 'pubs', 'nightclub', 'nightclubs']
clothingKey = ['clothing', 'clothes', 'shop', 'shops', 'shopping']
fitnessKey = ['fitness', 'gym', 'sport']
activitiesKey = ['activity', 'activities', 'museum', 'cathedral', 'gallery', 'theatre']
parksKey = ['park', 'reserve']

#print(str(name['drinking'][7]))                                             #Prints the column with a certain header name

'''Keywords entered in a list, information is found and returned in a list'''
def findInfo(keywords):

    '''Takes in entry as a string, removes unnecessary characters and returns entry as a string'''
    def fixEntry(entry):
        entry = entry.translate({ord(c): None for c in '\'[]"'}) #Take out any ',[ or ] characters in the string, code from https://stackoverflow.com/questions/3939361/remove-specific-characters-from-a-string-in-python
        entry = entry.strip('\n')   #Take out any line breaks in the string
        if entry[0] == 'b' and entry not in ['belgrade theatre', 'brandon marsh nature reserve', 'riley\'s sports bar']:   #Some strings gain the letter b when the numpy array is converted to a list
            entry = entry[1:]   #Remove the letter b from the front
        return entry
    
    #Look at each keyword and see if they belong to a catergory
    #If a category has been found, check to see if the results can be more specific to the keyword
    for word in keywords:  #For each keyword in the users input
        if word in drinkingKey:    #If the word is in one of the keys
            lis = list((str(name['drinking'])).split(' b')) #Create a list all all the information on that topic
            for entry in lis:   #Check to see if the information can be more specific based on the keyword#Check to see if the information can be more specific based on the keyword
                if word in entry:
                    entry = fixEntry(entry)     #Remove any unnecessary characters from the string
                    outputInfo.append(entry)    #Add the information to a list
            if outputInfo == []:    #If the information could not be more specific
                for entry in lis:   #Look at each entry in the list
                    if "''" not in entry:   #If the entry is not empty
                        outputInfo.append(fixEntry(entry))  #Add the information to the output
                    
        elif word in activitiesKey:
            lis = list((str(name['activites'])).split(' b'))
            for entry in lis:
                if word in entry:
                    entry = fixEntry(entry)
                    outputInfo.append(entry)
                if outputInfo == []:
                    for entry in lis:
                        if "''" not in entry:
                            outputInfo.append(fixEntry(entry))

        elif word in clothingKey:
            lis = list((str(name['clothing'])).split(' b'))
            for entry in lis:
                if word in entry:
                    entry = fixEntry(entry)
                    outputInfo.append(entry)
                if outputInfo == []:
                    for entry in lis:
                        if "''" not in entry:
                            outputInfo.append(fixEntry(entry))
                    
        elif word in fitnessKey:
            lis = list((str(name['fitness'])).split(' b'))
            for entry in lis:
                if word in entry:
                    entry = fixEntry(entry)
                    outputInfo.append(entry)
                if outputInfo == []:
                    for entry in lis:
                        if "''" not in entry:
                            outputInfo.append(fixEntry(entry))
                    
        elif word in parksKey:
            lis = (str(name['parks'])).split(' b')
            for entry in lis:
                if word in entry:
                    entry = fixEntry(entry)
                    outputInfo.append(entry)
                if outputInfo == []:
                    for entry in lis:
                        if "''" not in entry:
                            outputInfo.append(fixEntry(entry))
                        
        else:
            return ('No information found')

    return outputInfo



#print(findInfo(keywords))
