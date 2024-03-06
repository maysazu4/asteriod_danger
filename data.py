import json 
from asteroid import Asteroids
import os


def convert_asteroids_to_dict(asteroids):
    if isinstance(asteroids,Asteroids):
        
        dict = {'id' : asteroids.id,
                'name' : asteroids.name,
                'est_diameter_min': asteroids.est_diameter_min,
                'est_diameter_max' : asteroids.est_diameter_max,
                'miss_distance'  : asteroids.miss_distance,
                'relative_vekocity'  : asteroids.relative_vekocity
                }
   
    return dict


''' Gets a list of Asteroid objects and save them into a json file '''
def save_asteroids_data(asteroids_list):
    dict_list = []
    for a in asteroids_list:
        dict = convert_asteroids_to_dict(a)
        dict_list.append(dict)
    with open('asteroids_data.json', 'w') as f:
        f.write('[')
        i = 0
        for chunk in dict_list:
            json.dump(chunk, f , indent=6)
            i += 1
            if i == len(dict_list):
                break
            f.write(',')
        f.write(']')   



''' Loads all the saved asteroids from a file, and returns a list of Asteroid objects '''
def load_asteroids_data(file):
    with open(file) as user_file:
        file_contents = user_file.read()
    parsed_json = json.loads(file_contents)
    l = []
    for object in parsed_json:
        a = Asteroids(object['id'] , object['name'],object['est_diameter_min'],
                  object['est_diameter_max'],object['miss_distance'],
                  object['relative_vekocity'])
        l.append(a)
    return l 
    





