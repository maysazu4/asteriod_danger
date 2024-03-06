import os as o
import init
import data as d
from asteroid import Asteroids
import plot as p
from danger_index import astroids_calculate_danger_index

if __name__ == "__main__":
    ''' This runs only when you run the code the first time '''
    if o.path.isfile('asteroids_data.json') == False:
        init.init()
    
    ''' Get the information about the asteroids and save them into a list of Asteroid object'''
    asteroids_list = d.load_asteroids_data('asteroids_data.json')
    
    ''' The graphs'''
    p.min_diameter_velocity_graph(asteroids_list)
    p.miss_distance_max_diameter_graph(asteroids_list)
    names , danger_indeces = astroids_calculate_danger_index(asteroids_list)
    p.asteroids_name_danger_index_graph(names, danger_indeces)
    


    
    
