import  numpy as np
from nptyping import NDArray, Shape, assert_isinstance , Number
def translationMatrix(translation:NDArray):
    assert_isinstance(translation, NDArray[Shape["3"], Number])
    matrix = np.eye(4)
    matrix[:,3] = np.append(translation, 1)
    return matrix

def rotationXMatrix(theta:float):
    assert isinstance(theta, float)
    matrix = np.array([
        [1,0,0,0],
        [0, np.cos(theta), -np.sin(theta), 0],
        [0, np.sin(theta), np.cos(theta), 0],
        [0,0,0,1]
    ])
    return matrix

def rotationYMatrix(theta:float):
    assert isinstance(theta, float)
    matrix = np.array([
        [np.cos(theta),0,np.sin(theta),0],
        [0, 1, 0, 0],
        [-np.sin(theta), 0, np.cos(theta), 0],
        [0,0,0,1]
    ])
    return matrix


def rotationZMatrix(theta:float):
    assert isinstance(theta, float)
    matrix = np.array([
        [np.cos(theta),-np.sin(theta),0,0],
        [np.sin(theta), np.cos(theta), 0, 0],
        [0, 0, 1, 0],
        [0,0,0,1]
    ])
    return matrix



