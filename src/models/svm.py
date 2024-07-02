from sklearn.svm import SVC

def svm(C, kernel, degree, gamma, max_iter):
    return SVC(C=C, kernel=kernel, degree=degree, gamma=gamma,
               max_iter=max_iter)