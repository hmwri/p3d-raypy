import numpy as np

from p3dray.camera import Camera
from p3dray.scene import Scene
from p3dray.utils import *
from p3dray.geometry.object import Object
from .raycaster import RayCaster
import p3dray.world as world


class RayTracer:
    def __init__(self, camera: Camera, scene: Scene):
        self.camera = camera
        self.scene = scene




    def trace_step(self, p0: np.ndarray, E: np.ndarray, depth) -> np.ndarray:

        if depth == 0:
            return np.zeros((E.shape[0], 3))
        ts = np.full((E.shape[0]), np.inf)
        ps = np.full((E.shape[0], 3), np.inf)
        surface_is = np.full((E.shape[0]), -1, dtype=int)

        pixel = np.full((E.shape[0], 3), 1.0)
        for object in self.scene.objects:
            aabb_intersect, aabb_intersect_index = is_intersect_aabb(object.aabb, p0, E)

            if aabb_intersect.sum() == 0:
                continue

            for i, surface in enumerate(object.surfaces) :
                aabb_intersect, aabb_intersect_index = is_intersect_aabb(surface.aabb, p0, E)
                N = surface.n

                is_intersect, t, p = RayCaster.cast(p0, E, surface.array_data, N, mask=aabb_intersect)
                if t is None:
                    continue
                t_resized = np.full((E.shape[0]), np.Inf)
                p_resized = np.full((E.shape[0], 3), np.inf)
                t_resized[is_intersect] = t.flatten()
                p_resized[is_intersect, :] = p

                smaller_t = (t_resized < ts.flatten())
                ts[smaller_t] = t_resized[smaller_t]
                ps[smaller_t, :] = p_resized[smaller_t]
                surface_is[smaller_t] = i

        for object in self.scene.objects:
            for i, surface in enumerate(object.surfaces):
                P = ps[surface_is == i]
                if E[surface_is == i].shape[0] == 0:
                    continue
                bc = surface.material.texture.get_color(surface.vertexes, P)
                mr = surface.material.metalic
                tr = surface.material.transmission
                ior = surface.material.IOR
                rn = surface.material.roughness







                if mr != 0:
                    R = calc_reflection_vector(E[surface_is == i], surface.n)
                    P1 = P + 0.01 * R
                    reflection = self.trace_step(P1, R+ 0.1 * rn * np.random.randn(*P.shape), depth-1)
                else:
                    reflection = np.zeros((P.shape[0],3))
                if tr != 0:
                    T = calc_IOR_vector(E[surface_is == i], surface.n, ior)
                    P2 = P + 0.01 * T
                    trans = self.trace_step(P2, T, depth-1)
                else:
                    trans = np.zeros((P.shape[0],3))


                color = (1-tr)*((1-mr) * bc + bc * mr * reflection) + bc * tr* trans
                pixel[surface_is == i, :] = color
        if (surface_is == -1).sum() != 0:
            if isinstance(self.scene.world.texture, world.SingleColorTexture):
                pixel[surface_is == -1, :] = self.scene.world.texture.color
            elif isinstance(self.scene.world.texture, world.EnvironmentTexture):
                pixel[surface_is == -1, :] = self.scene.world.texture.get_color(E[surface_is == -1])
        return pixel

    def _trace_step_wrapper(self, args):
        return self.trace_step(*args)

    def trace(self, N) -> np.ndarray:

        pixel = np.zeros([self.camera.E.shape[0], 3])
        for i in range(N):
            pixel += self.trace_step(np.zeros_like(self.camera.E),
                            self.camera.E + 0.001 * np.random.randn(*self.camera.E.shape), depth=3)
        return pixel/N