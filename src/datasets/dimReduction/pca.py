from sklearn.decomposition import PCA

def pca(whiten, svd_solver):
    return PCA(whiten=whiten, svd_solver=svd_solver)