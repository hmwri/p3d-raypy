import numpy as np
from p3dray.utils import normalize
from p3dray.math import vector


class Camera:

    def __init__(self, theta, aspect, resolution):
        self.__theta = theta
        self.__aspect = aspect
        self.resolution = resolution
        self.E = self.__calc_vec_from_eye_to_pixel()


    def __calc_vec_from_eye_to_pixel(self):
        d = vector.vec3(0, 0, 1)

        w = 2*np.tan(self.__theta/2)
        h = w*self.__aspect
        print(w, h)
        x = np.linspace(-w/2, w/2, self.resolution[0])
        y = np.linspace(-h/2, h/2, self.resolution[1])[::-1]
        xx, yy = np.meshgrid(x, y)
        xxyy = np.c_[xx.flatten(), yy.flatten(), np.zeros(self.resolution[0] * self.resolution[1])]
        r = xxyy[:] + d.T
        return normalize(r, axis=1)



class CameraManager:
    camera : Camera = Camera(np.radians(90), 9 / 16, (1600, 900))


def camera(theta, aspect, resolution):
    CameraManager.camera = Camera(theta, aspect, resolution)