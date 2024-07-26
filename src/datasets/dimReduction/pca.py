"""
File providing a function that returns an instance of an object that represents the PCA algorithm.
"""
from sklearn.decomposition import PCA

def pca(whiten, svd_solver):
    """Instantiate a PCA object

    :param whiten: _description_
    :type whiten: boolean
    :param svd_solver: Solver used for PCA
    :type svd_solver: str
    :return: PCA object
    :rtype: <PCA>
    """
    return PCA(whiten=whiten, svd_solver=svd_solver, n_components=2)