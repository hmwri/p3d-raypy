import math

import  numpy as np

def normalize(v:np.ndarray, axis=None) -> np.ndarray:
    return v / np.linalg.norm(v, axis=axis, keepdims=True)

def calc_normalized_cross(v1: np.ndarray, v2:np.ndarray, axis=None) -> np.ndarray:
    cross = np.cross(v1, v2)
    return normalize(cross, axis=axis)

def get_plane_function(N: np.ndarray, p1:np.ndarray):
    func = lambda p : np.sum(N * (p - p1.T).T, axis=0)
    return func



def create_plane_equation(normal_vector, points):
    # 重心を計算
    centroid = np.mean(points, axis=0)

    # 法線ベクトルの成分を1次元配列に変換
    normal_vector_1d = normal_vector.flatten()

    # d を計算
    d = -np.dot(normal_vector_1d, centroid)

    # 平面の方程式を表す関数を定義
    def plane_equation(pts):
        # 各点に対して平面方程式の値を計算
        return np.dot(pts, normal_vector_1d) + d

    return plane_equation

def is_intersect_aabb(aabb:np.ndarray,p0:np.ndarray, d: np.ndarray, mask=None) -> tuple[np.ndarray, np.ndarray]:
    if mask is not None:
        base_intersected = np.zeros(d.shape[0], dtype=bool)
        p0 = p0[mask]
        d = d[mask]

    min : np.ndarray = aabb[0].reshape(1,3)
    max : np.ndarray = aabb[1].reshape(1,3)
    t_min = ((min - p0).reshape(-1,3) / d )
    t_max = ((max - p0).reshape(-1,3) / d)
    t_input = t_min.copy()
    t_output = t_max.copy()
    t_input[t_min > t_max] = t_max[t_min > t_max]
    t_output[t_min > t_max] = t_min[t_min > t_max]
    t_output[t_output == np.nan] = 0
    intersected : np.ndarray = ((np.min(t_output, axis=1) - np.max(t_input, axis=1)) >= 0)

    if mask is not None:
        base_intersected[mask] = intersected
        return base_intersected, np.arange(base_intersected.shape[0])[base_intersected]

    return intersected, np.arange(intersected.shape[0])[intersected]


def slice_last_dimension(arr, i):
    if arr.ndim == 1:
        return arr[i]
    elif arr.ndim == 2:
        return arr[:, i]
    elif arr.ndim == 3:
        return arr[:, :, i]


def RC2SC(xyz:np.ndarray) -> np.ndarray:
    axis = xyz.ndim - 1
    x = slice_last_dimension(xyz,0)
    y = slice_last_dimension(xyz,2)
    z = slice_last_dimension(xyz, 1)

    print(f"{np.min(x)}")

    r = np.linalg.norm(xyz, axis=axis)
    theta = np.arccos(z/r)[:, np.newaxis]
    phi = (np.sign(y) * np.arccos(x/np.sqrt(x*x + y*y)))[:, np.newaxis]
    return np.hstack([r[:, np.newaxis], theta, phi])

def calc_reflection_vector(E:np.ndarray,N:np.ndarray) -> np.ndarray:
    R = E + (2*(-E @ N).T*N).T
    return normalize(R, axis=1)

def calc_IOR_vector(E:np.ndarray,N:np.ndarray, eta:float) -> np.ndarray:
    result = np.zeros((E.shape[0], 3))
    k = E @ N
    a = (1 - eta ** 2 * (1 - k ** 2))
    not_minus = (a >= 0).flatten()

    result[not_minus] = eta*E[not_minus, :] + (eta*k[not_minus] - np.sqrt(a[not_minus]))*N.T
    result[~not_minus] = calc_reflection_vector(E[~not_minus, :], N)
    return normalize(result, axis=1)


def radians(theta):
    return math.radians(theta)