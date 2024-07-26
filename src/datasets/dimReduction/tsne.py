"""
File providing a function that returns an instance of an object that represents the TSNE algorithm.
"""
from sklearn.manifold import TSNE

def tsne(perplexity, max_iter, n_iter_without_progress, init, method):
    """Instantiate a TSNE object

    :param perplexity: The perplexity is related to the number of nearest neighbors that is used in other manifold learning algorithms.
    :type perplexity: int (should be float)
    :param max_iter: Maximum number of iterations before automatically stopping
    :type max_iter: int
    :param n_iter_without_progress: Number of iterations allowed before stopping if no progess is made
    :type n_iter_without_progress: int
    :param init: Initialization of embedding
    :type init: str
    :param method: Method used to compute TSNE
    :type method: str
    :return: TSNE object
    :rtype: <TSNE>
    """
    return TSNE(perplexity=perplexity, max_iter=max_iter, n_iter_without_progress=n_iter_without_progress,
                init=init, method=method, n_components=2)