from sklearn.manifold import Isomap

def isomap(n_neighbors, radius, eigen_solver, max_iter, path_method, neighbors_algorithm):
    return Isomap(n_neighbors=n_neighbors, radius=radius, eigen_solver=eigen_solver,
                  max_iter=max_iter, path_method=path_method, neighbors_algorithm=neighbors_algorithm,
                  n_components=2)