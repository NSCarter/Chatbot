#import the library used to access webpages and decode the data
import urllib.request
import json

userInput = 'singer+hall' #the input from the user

#acces the website
with urllib.request.urlopen('https://maps.googleapis.com/maps/api/place/radarsearch/json?location=52.408040,-1.511378&radius=10000&rankby=prominence&keyword='+userInput+'&key=AIzaSyDtTDDYIt-fYijfy9c-mpBkZKOAoNhj1j8') as response:
    raw = response.read()   #read the data from the website

data = json.loads(raw.decode('utf-8'))  #decode the data into a dictionary

#Finds the ID and the location of the first result
placeID = data['results'][0]['place_id']
reference = data['results'][0]['reference']
geometry = data['results'][0]['geometry']
iD = data['results'][0]['id']
#print the ID and the location
print('\n'+placeID)
print(reference+'\n')
print(geometry,'\n')
print(iD+'\n')
