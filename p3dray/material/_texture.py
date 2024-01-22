import numpy as np
import PIL.Image as Image

class Texture:
    def __init__(self):
        pass


    def get_color(self, vertexes : list[np.ndarray], p : np.ndarray) -> np.ndarray:
        pass


class UVTexture(Texture):
    def __init__(self,  image:np.ndarray | str, uv : list[np.ndarray]):
        super().__init__()
        if isinstance(image, str):
            image = np.array(Image.open(image))
        self.image = image
        self.uv = uv

    def get_color(self,vertexes : list[np.ndarray], p : np.ndarray) -> np.ndarray:
        return p


class SingleColorTexture(Texture):
    def __init__(self, color:np.ndarray):
        super().__init__()
        self.color = color


    def get_color(self, vertexes : list[np.ndarray], p : np.ndarray) -> np.ndarray:
        return self.color