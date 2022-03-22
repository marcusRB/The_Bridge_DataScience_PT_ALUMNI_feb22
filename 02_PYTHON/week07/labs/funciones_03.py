
import math
def compute_all_distances(x, y):
    
    def eucl_dist(x, y):
    # Definimos la función que calcula la distancia utilizando una list
    # comprehension uniendo los valores de los vectores x e y con zip
        return math.sqrt(sum([(coord[0]-coord[1])**2 for coord in zip(x,y)]))

    def manh_dist(x,y):
        return sum([abs(coord[0] - coord[1]) for coord in zip(x,y)])

    return (eucl_dist(x,y), manh_dist(x,y))

vec1 = [5, 2, -3, 4]
vec2 = [1, 6, -7, 8]
compute_all_distances(vec1, vec2)