import requests
import json #this module will let us convert the json into a string
import pandas as pd 


#output = 'yelpResponse.csv'
#yelp_data = []

api_key=""
headers = {'Authorization': 'Bearer %s' % api_key}

#Saving the URL as a variable
url='https://api.yelp.com/v3/businesses/search'
 
# In the dictionary, term can take values like food, cafes or businesses like McDonalds
params = {'latitude': 40.853288, 'longitude': -73.411211,'limit':2}

#standard syntax for the requests library. Could also write 'r = requests.get('https://..)
# Making a get request to the API
r = requests.get(url, params=params, headers=headers)
packages_json = r.json()

# proceed only if the status code is 200
print('The status code is {}'.format(r.status_code))


packages_str = json.dumps(packages_json, indent=2)
print(packages_str)

#printing the text from the response
#response_json = req.json()
#print(response_json)
#jsonResponse = json.loads(req.text)
#print (jsonResponse)

d1 = {'latitude': 41.853288, 'latitude': 42.853288}
params.update(d1)
print (params)


for x in params:
    print(x, params[x])
    
    
    for x in params:
    params.popitem()
    print(params)
    params.update(d1)
    print(params)
