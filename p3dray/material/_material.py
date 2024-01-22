import numpy as np
from ._texture import Texture, SingleColorTexture, UVTexture



class Material:
    def __init__(self, metalic = 0.5, roughness=0.5, transmission=0, ior=1, texture : Texture =SingleColorTexture(np.zeros(3))):

        self.metalic = metalic
        self.roughness = roughness
        self.transmission = transmission
        self.IOR = ior
        self.texture : Texture = texture



class MaterialManager:
    material = Material()



def set_material(base_color=np.zeros(3), metalic = 0.5,roughness=0.5, transmission=0, ior=1, texture=None):
    if not isinstance(base_color, np.ndarray) :
        base_color = np.array(base_color)
    if texture is None :
        texture = SingleColorTexture(base_color)
    MaterialManager.material = Material(metalic=metalic, roughness=roughness, transmission=transmission, ior=ior, texture=texture)
