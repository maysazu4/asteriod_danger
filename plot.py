import matplotlib.pyplot as plt

''' Plots the graph of velocity vs minimum diameter'''
def min_diameter_velocity_graph(asteroids_list):
    diameter = []
    velocity = []
    for a in asteroids_list:
        diameter.append(float(a.est_diameter_min))
        velocity.append(float(a.relative_vekocity))
    plt.scatter(diameter,velocity,color = 'maroon')
    plt.ylabel('Velocity')
    plt.xlabel('Min diameter')
    plt.show()


''' Plots the graph of maximum diameter vs miss distance'''
def miss_distance_max_diameter_graph(asteroids_list):
    miss_distance = []
    max_diameter = []
    for a in asteroids_list:
        miss_distance.append(float(a.miss_distance))
        max_diameter.append(float(a.est_diameter_max))
    plt.scatter(miss_distance,max_diameter,color = 'maroon')
    plt.ylabel('max diameter')
    plt.xlabel('miss distance')
    plt.show()

''' Plots the graph of Danger index vs asteroid name'''
def asteroids_name_danger_index_graph(names , danger_indeces):
    plt.bar(names,danger_indeces,color ='maroon', 
        width = 0.3)
    plt.ylabel('Danger indeces')
    plt.xlabel('Asteroids names')
    plt.show()
