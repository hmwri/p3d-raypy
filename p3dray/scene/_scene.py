from p3dray.geometry.vertex import Vertex
import numpy as np
from p3dray.geometry.surface import Surface
from p3dray.geometry.object import Object
from p3dray.material import Material
from p3dray.world import World, SingleColorTexture, EnvironmentTexture


class Scene :

    def __init__(self):
        self.objects:list[Object] = []
        # self.surfaces.append(Surface(
        #     Vertex(2, 2, 10),
        #         Vertex(2, -2, 10),
        #     Vertex(-10,   -2, 20),
        #     material=Material(base_color=np.array([1, 1, 1]), metalic=0)
        # ))
        # self.surfaces.append(Surface(
        #     Vertex(2, -2, -10),
        #     Vertex(-10, -2, -10),
        #     Vertex(2, 2, -10),
        #
        #     material=Material(base_color=np.array([1, 1, 1]), metalic=1)
        #
        # ))
        # self.surfaces.append(Surface(
        #         Vertex(-1,  1,  1),
        #         Vertex( 1,  1,  1),
        #         Vertex( 1, -1,  1),
        # ))
        self.world = World(SingleColorTexture(np.array([0.8,0.8,1])))




scene = Scene()


def set_world_color(color):
    scene.world = World(SingleColorTexture(np.array(color)))


def set_environment_texture(path):
    scene.world = World(EnvironmentTexture(path))





