import numpy as np
from multiprocessing import Pool
import cv2
from p3dray.raytracer import RayTracer
from p3dray.camera import CameraManager
from p3dray.scene import scene


def render(sample_N=1):
    cam = CameraManager.camera
    raytracer = RayTracer(cam, scene)
    pixel = raytracer.trace(sample_N)
    pixel = pixel.reshape((cam.resolution[1], cam.resolution[0], 3))
    cv2.namedWindow("main", cv2.WINDOW_NORMAL)
    pixel = (pixel * 255).astype(dtype=np.uint8)
    pixel = cv2.cvtColor(pixel, cv2.COLOR_RGB2BGR)
    cv2.imshow("main", pixel)
    cv2.resizeWindow("main", cam.resolution[0], cam.resolution[1])
    cv2.waitKey()
