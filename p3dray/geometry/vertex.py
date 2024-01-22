import numpy as np
from p3dray.coordinate import MatrixManager

class Vertex:
    def __init__(self, x, y, z):
        print(MatrixManager.matrix)
        self.point = MatrixManager.matrix @ np.array([x,y,z,1]).reshape(-1,1)

