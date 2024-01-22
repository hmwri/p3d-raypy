from p3dray.utils.matrix import *



class MatrixManager:


    matrix = np.eye(4)

def translate(x, y, z):
    _matrix = translationMatrix(np.array([x,y,z]))
    MatrixManager.matrix = _matrix @ MatrixManager.matrix


def rotateX(theta):
    _matrix = rotationXMatrix(theta)
    MatrixManager.matrix = _matrix @ MatrixManager.matrix


def rotateY(theta):
    _matrix = rotationYMatrix(theta)
    MatrixManager.matrix = _matrix @ MatrixManager.matrix

def rotateZ(theta):
    _matrix = rotationZMatrix(theta)
    MatrixManager.matrix = _matrix @ MatrixManager.matrix


