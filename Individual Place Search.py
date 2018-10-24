#Import the library used to access webpages and decode the data
import urllib.request
import json

userInput = 'coventry student union' #The input from the user
userInput = userInput.replace(' ', '+') #Turn the input into something that can be used in the url

def individualPlaceSearch(userInput):
    '''Takes an input from a user as a string, finds information about a place, and returns it as a list of strings'''
    
    userInput = userInput.replace(' ', '+') #Turn the input into something that can be used in the url
    output = []
    
    #Access the results from the following web address
    with urllib.request.urlopen('https://maps.googleapis.com/maps/api/place/radarsearch/json?location=52.408040,-1.511378&radius=10000&rankby=prominence&keyword='+userInput+'&key=AIzaSyDtTDDYIt-fYijfy9c-mpBkZKOAoNhj1j8') as response:
        raw = response.read()   #Read the data

    data = json.loads(raw.decode('utf-8'))  #Decode the data into a dictionary

    #Finds the ID and the location of the first result
    placeID = data['results'][0]['place_id']

    #Access the results from the following web address
    with urllib.request.urlopen('https://maps.googleapis.com/maps/api/place/details/json?placeid='+placeID+'&key=AIzaSyDtTDDYIt-fYijfy9c-mpBkZKOAoNhj1j8') as response:
        raw2 = response.read()   #Read the data

    data2 = json.loads(raw2.decode('utf-8'))    #Decode the data into a dictionary

    #The information to be found for the user
    information = ['name','rating','formatted_address','open_now','formatted_phone_number','website']

    #Check if the information we want to find is available in the data2 variable and output the information
    for i in information:
        if i == 'open_now':
            if 'opening_hours' in data2['result']:
                if data2['result']['opening_hours'][i] == True:
                    output.append('Open now')
                else:
                    output.append('Closed now')
        else:
            if i in data2['result']:
                if i == 'rating':
                    output.append((data2['result'][i], 'stars'))
                else:
                    output.append(data2['result'][i])

    return output

print(individualPlaceSearch(userInput))
