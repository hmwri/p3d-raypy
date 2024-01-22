import numpy as np
from PIL import Image
from p3dray.utils import RC2SC


class World:
    def __init__(self, texture : 'Texture'):
        self.texture = texture
        pass


class Texture:
    def __init__(self):
        pass


class EnvironmentTexture(Texture):
    def __init__(self, path):
        super().__init__()
        self.image : np.ndarray = np.array(Image.open(path))

        self.image = self.image/255

        self.width = self.image.shape[1]
        self.height = self.image.shape[0]
        print(self.image.shape)

    def get_color(self, E:np.ndarray):
        sc = RC2SC(E)
        x = ((sc[:,2] + np.pi) / (2*np.pi) * self.width).astype(dtype=int)
        y = (sc[:,1] / np.pi * self.height).astype(dtype=int)
        index = y * self.width + x
        return self.image.reshape([-1,3])[index]






class SingleColorTexture(Texture):
    def __init__(self, color:np.ndarray):
        super().__init__()
        self.color : np.ndarray = color
