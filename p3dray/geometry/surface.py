import copy

import numpy as np
from p3dray.utils import normalize
from .vertex import Vertex
from p3dray.material import Material, MaterialManager
class Surface:
    def __init__(self, *points:Vertex):

        material = MaterialManager.material
        self.vertexes = []
        array_data = np.zeros((len(points), 3))
        for i, point in enumerate(points):
            assert isinstance(point, Vertex)
            array_data[i] = point.point[:3].flatten()
            self.vertexes.append(point)
        self.array_data : np.ndarray = array_data
        self.aabb = np.min(self.array_data.reshape(-1,3),axis=0)

        self.aabb = np.vstack([self.aabb, np.max(self.array_data.reshape(-1,3),axis=0)])

        self.material =copy.deepcopy(material)

        self.n = normalize(np.cross((array_data[1] - array_data[2])
                          , (array_data[-1] - array_data[0]).T
                          )).reshape(-1,1)




