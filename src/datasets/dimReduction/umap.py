"""
File providing a function that returns an instance of an object that represents the UMAP algorithm.
"""
from umap import UMAP

def umap(n_neighbors, min_dist, metric):
    """Instantiate a UMAP object

    :param n_neighbors: Number of neighbors that is going to be used for each data point
    :type n_neighbors: int
    :param min_dist: Control how tightly UMAP is allowed to pack points together
    :type min_dist: int (should be float)
    :param metric: Metric used to compute distances
    :type metric: str
    :return: UMAP object
    :rtype: <UMAP>
    """
    return UMAP(n_neighbors=n_neighbors, min_dist=min_dist, metric=metric, n_components=2)