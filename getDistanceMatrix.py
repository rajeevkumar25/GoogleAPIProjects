# Basic feature :- This program would accept three parameters origin,destination and mode of transport
# and return the distance and duration it would take with given mode
# Using Google distance matrix api

import requests
import json
from key import google_maps_dist_matrix_api_key

#sample_request='https://maps.googleapis.com/maps/api/distancematrix/json?units=indian&origins=ranchi&destinations=patna&mode=car&key=API-KEY'

req_base_url='https://maps.googleapis.com/maps/api/distancematrix/json?'

def getDistanceMatrix(requesturl):
    try:
        api_response=requests.get(requesturl)
        api_res_json=api_response.json()
        #print(api_res_json)       
        if api_res_json['status']=='OK':
            #print(api_res_json['rows'])
            details=api_res_json['rows']
            
            for detail in details:
                #print(detail['elements'][0].text)
                actual_detail=detail['elements'][0]
                
                print('Duration:- '+actual_detail['duration']['text'])
                print('Distance:- '+actual_detail['distance']['text'])
            
        else:
            print('Exception')
    except Exception:
        pass
    
if __name__=='__main__':
    origin=raw_input('Please Enter Origin:- ').strip()
    destination=raw_input('Please Enter Destination:- ').strip()
    mode=raw_input('Enter mode of transport:- ').strip()

    if (origin and destination):
        request_url=req_base_url+'origins='+origin+'&destinations='+destination+'&mode='+mode+'&key='+google_maps_dist_matrix_api_key
        getDistanceMatrix(request_url)
    else:
        print('Not a valid search!')
    #print(request_url)

