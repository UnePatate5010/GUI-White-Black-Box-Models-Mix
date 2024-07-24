from sklearn.manifold import TSNE

def tsne(perplexity, n_iter, n_iter_without_progress, init, method):
    return TSNE(perplexity=perplexity, n_iter=n_iter, n_iter_without_progress=n_iter_without_progress,
                init=init, method=method)