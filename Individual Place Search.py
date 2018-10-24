#import the library used to access webpages and decode the data
import urllib.request
import json

userInput = 'where+is+the+wheather' #the input from the user

#acces the website
with urllib.request.urlopen('https://maps.googleapis.com/maps/api/place/radarsearch/json?location=52.408040,-1.511378&radius=10000&rankby=prominence&keyword='+userInput+'&rst=1&key=AIzaSyDtTDDYIt-fYijfy9c-mpBkZKOAoNhj1j8') as response:
    raw = response.read()   #read the data from the website

data = json.loads(raw.decode('utf-8'))  #decode the data into a dictionary

#look at each item in the dictionary
for i in range(len(data['results'])):
    #find the place ID and and the location
    placeID = data['results'][i]['place_id']
    reference = data['results'][i]['reference']
    geometry = data['results'][i]['geometry']
    iD = data['results'][i]['id']
    #print the place ID and the location
    print('\n'+placeID)
    print(reference+'\n')
    print(geometry,'\n')
    print(iD+'\n')
