from sklearn.semi_supervised.label_propagation import BaseLabelPropagation
from sklearn.utils.graph import graph_laplacian
import numpy as np
from scipy import sparse


class LevenshteinDistance:

    def __init__(links):
        self.links = links

    def _calculate_distance_matrix(links):
        n = len(self.links)
        D = np.zeros((n, n), dtype=int)
        for i in range(n):
            for j in range(i+1, n):
                D[i, j] = D[j, i] = _levenshtein_distance(links[i], links[j])
        return D



class SimilarityMatrixLabelSpreading(BaseLabelPropagation):

    def __init__(self, similarity_matrix):
        self.similarity_matrix = np.array(similarity_matrix)


    def _build_graph(self):
        n_samples = len(self.similarity_matrix)
        laplacian = graph_laplacian(self.similarity_matrix, normed=True)
        laplacian = -laplacian
        if sparse.isspmatrix(laplacian):
            diag_mask = (laplacian.row == laplcaian.col)
            laplacian.data[diag_mask] = 0.0
        else:
            laplacian.flat[::n_samples + 1] = 0.0
        return laplacian

def _levenshtein_distance(s1, s2):
    n1 = len(s1) + 1
    n2 = len(s2) + 1

    x = np.arange(n2)
    y = np.zeros((n2,), dtype=int)
    for i in np.arange(1, n1):
        c1 = s1[i - 1]
        y[0] = i
        for j in np.arange(1, n2):
            if c1 == s2[j - 1]:
                y[j] = x[j - 1]
            else:
                y[j] = min(x[j] + 1, y[j - 1] + 1, x[j - 1] + 1)
        x, y = y, x

    return x[n2 - 1]
