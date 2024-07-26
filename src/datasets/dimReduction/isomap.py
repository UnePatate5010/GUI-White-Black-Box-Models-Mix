"""
File providing a function that returns an instance of an object that represents the Isomap algorithm.
"""
from sklearn.manifold import Isomap

def isomap(n_neighbors, radius, eigen_solver, max_iter, path_method, neighbors_algorithm):
    """Instantiate an Isomap object

    :param n_neighbors: Number of meighbors considered for each point
    :type n_neighbors: int or None
    :param radius: Limit distance of neighbors to use.
    :type radius: int (should be float) or None
    :param eigen_solver: Method used for the Eigen Solver
    :type eigen_solver: str
    :param max_iter: Maximum number of iterations before automatically stopping
    :type max_iter: int
    :param path_method: Method to use in finding shortest path
    :type path_method: str
    :param neighbors_algorithm: Algorithm to use for nearest neighbors search
    :type neighbors_algorithm: str
    :return: Isomap object
    :rtype: <Isomap>
    """
    return Isomap(n_neighbors=n_neighbors, radius=radius, eigen_solver=eigen_solver,
                  max_iter=max_iter, path_method=path_method, neighbors_algorithm=neighbors_algorithm,
                  n_components=2)