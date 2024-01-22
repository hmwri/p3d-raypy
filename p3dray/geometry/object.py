import numpy as np

from .surface import Surface

class Object:
    def __init__(self, surfaces:list[Surface]):
        aabb_max =  np.array([-np.inf, -np.inf, -np.inf])
        aabb_min = np.array([np.inf, np.inf, np.inf])
        for s in surfaces:
            aabb_min[aabb_min > s.aabb[0]] = s.aabb[0][aabb_min > s.aabb[0]]
            aabb_max[aabb_max < s.aabb[1]] = s.aabb[1][aabb_max < s.aabb[1]]
        self.aabb = np.vstack([aabb_min, aabb_max])
        self.surfaces = surfaces

        print("aabb", self.aabb)





