''' Calculate the danger index for specific asteroid according to the formula'''
def get_danger_index(min_diameter,max_diameter,relative_velocity,miss_distacne,A,B,C):
    avg_diameter = (min_diameter + max_diameter)/2
    return A*float(avg_diameter) + B* float(relative_velocity) + (1/C)* float(miss_distacne)


''' Returns two lists one contains the names of asteroids and the second has the danger index of each asteroid'''
def astroids_calculate_danger_index(asteroids_list,A = 10,B = 3, C = 10):
     names = []
     danger_indeces = []
     for a in asteroids_list:
          danger_index = get_danger_index(a.est_diameter_min, a.est_diameter_max,a.relative_vekocity,a.miss_distance,A,B,C)
          names.append(a.name)
          danger_indeces.append(danger_index)
     return names,danger_indeces

        
