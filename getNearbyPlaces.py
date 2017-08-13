# first google place api program
# basic feature: Provide the what are you searching for like restaurants,school,park,hostpital etc and in which area like pimple gurav,
# pimple saudagar, kharadi and it will output name , rating and address of the place you have searched in given area

import requests
import json
from key import api_key

google_api_key=api_key
google_api_base_url='https://maps.googleapis.com/maps/api/place/textsearch/json?query='



def getPlaces(apiurl):
    #print(apiurl)
    api_response=requests.get(apiurl)
    if api_response.status_code==200:
        api_response_json=api_response.json()
        
        rest_details=api_response_json['results']
        for details in rest_details:
            print(str(details['name']))
            if 'rating' in details:
                print('Rating: ' + str(details['rating']))
            else:
                print('No rating!')
            if 'formatted_address' in details:
                print('Address: '+str(details['formatted_address']))
            else:
                print('No Address found!')    
            print('==============')
 
if __name__=='__main__':
    place_type=raw_input('Please Enter what you want to search:-').strip()
    place_area=raw_input('You want to search '+ place_type + ' in which area?').strip()

    if place_type!="":
        google_api=google_api_base_url+place_type+'+in+'+place_area+'&'+'key='+google_api_key
        getPlaces(google_api)
    else:
        print('Opps! Not a valid search!')