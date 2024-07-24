from umap import UMAP

def umap(n_neighbors, min_dist, metric):
    return UMAP(n_neighbors=n_neighbors, min_dist=min_dist, metric=metric)