"""
File providing a function that returns an instance of an object that represents a SVM.
"""
from sklearn.svm import SVC

def svm(C, kernel, degree, gamma, max_iter):
    """Instantiate a SVM with the provided parameters
    
    :param C: Regularization parameter
    :type C: int or float
    :param kernel: The chosen kernel to apply
    :type kernel: str
    :param degree: The degree for the kernel (only for 'poly' kernel)
    :type degree: int
    :param gamma: Kernel coefficient for 'rbf', 'poly' and 'sigmoid'
    :type gamma: str
    :param max_iter: Maximum iteration in case it never ends
    :type max_iter: int
    :return: A SVC classifier with the right parameters
    :rtype: class <SVC>
    """
    return SVC(C=C, kernel=kernel, degree=degree, gamma=gamma,
               max_iter=max_iter)