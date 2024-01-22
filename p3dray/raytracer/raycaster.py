import numpy as np
from p3dray.utils import normalize

class RayCaster:

    @staticmethod
    def cast(p0:np.ndarray, E:np.ndarray, surface:np.ndarray, N:np.ndarray, mask:np.ndarray = None) -> tuple[np.ndarray, np.ndarray | None, np.ndarray |None]:
        """
        レイを飛ばして判定を行う
        :param E: レイ (N*3)
        :param surface: 面(V*3)
        :param N: 面の法線ベクトル (3*1)
        :return:
        """

        intersect_matrix_base = np.zeros(E.shape[0], dtype=bool)
        if mask is not None:
            p0 = p0[mask, :]
            E = E[mask, :]

        p1 = surface[0, :]
        t = -(p0 - p1[np.newaxis, :]) @ N / (E @ N)
        is_t_positive = (t>0).flatten()
        if is_t_positive.sum() == 0:
            return intersect_matrix_base, None, None
        is_t_positive_index = np.arange(t.shape[0])[is_t_positive]
        P = p0[is_t_positive, :] + t[is_t_positive] * E[is_t_positive, :]

        p_i = surface
        p_j = np.vstack([surface[1:, :], surface[0, :]])
        # vec(i->j), V * 3
        p_ij = p_j - p_i
        # vec(i->P), N * V * 3
        p_iP = P[:, np.newaxis, :] - p_i[np.newaxis, :, :]

        crosses = normalize(np.cross(p_ij, p_iP, axisa=1, axisb=2), axis=2)
        base_cross = crosses[:,0,:][:, np.newaxis, :]


        cos_similarity = np.sum(crosses * base_cross, axis=2)

        true_matrix = np.zeros(E.shape[0], dtype=bool)
        is_intersect = np.abs(cos_similarity.shape[1] - np.sum(cos_similarity,axis=1)) < 0.0001
        intersect_index = is_t_positive_index[is_intersect]
        true_matrix[intersect_index] = True

        if mask is not None:
            intersect_matrix_base[mask] = true_matrix
            return intersect_matrix_base, t[intersect_index], P[is_intersect, :]



        return true_matrix , t[intersect_index], P[true_matrix, :]


