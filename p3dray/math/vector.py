import numpy as np

from nptyping import NDArray,Shape, Number

Vector3 = NDArray[Shape["3"], Number]

def vec3(x, y, z) -> Vector3:
    return np.array([x,y,z]).reshape(-1, 1)