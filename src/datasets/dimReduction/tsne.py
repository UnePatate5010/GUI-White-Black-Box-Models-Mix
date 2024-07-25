from sklearn.manifold import TSNE

def tsne(perplexity, max_iter, n_iter_without_progress, init, method):
    return TSNE(perplexity=perplexity, max_iter=max_iter, n_iter_without_progress=n_iter_without_progress,
                init=init, method=method, n_components=2)