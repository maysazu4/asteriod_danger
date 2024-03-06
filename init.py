import requests
import datetime 
import urllib
import data as d
from asteroid import Asteroids
import json
from Api_key import api_key


''' The get request query parameters '''
START_DATE = datetime.date(2024,3,5)   
END_DATE = datetime.date(2024,3,10)
query_parameters = {
        "start_date" : datetime.date(2024,3,5),
        "end_date": END_DATE,
        "api_key": api_key,
}


''' Get the data using get request '''
def api_request_and_get_data():
    url = "https://api.nasa.gov/neo/rest/v1/feed?{}".format(urllib.parse.urlencode(query_parameters))
    response = requests.get(url)
    data = response .json()
    return data


''' Save the asteroids data to a json file '''
def save_data_to_file(data):
     l = []
     for appid,value in data['near_earth_objects'].items():
        a = Asteroids(value[0]['id'],
        value[0]['name'],
        value[0]['estimated_diameter']['kilometers']['estimated_diameter_min'],
        value[0]['estimated_diameter']['kilometers']['estimated_diameter_max'],
        value[0]['close_approach_data'][0]['miss_distance']['kilometers'],
        value[0]['close_approach_data'][0]['relative_velocity']['kilometers_per_hour'])
        l.append(a)

     d.save_asteroids_data(l)


''' Calls the functions above, at the end of this function we have a json file with the asteroids data '''
def init():
    data = api_request_and_get_data()
    save_data_to_file(data)
    
    




   
   

