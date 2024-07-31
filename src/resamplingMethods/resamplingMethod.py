"""Interface for resampling method
    """

class resamplingMethod:

    def fit_resample(self, X, y):
        """This method perform a data resampling over the dataset X. This method is in charge to
        check the number of point in the class to augment. In case there is not enough, it should either
        diminish its number of neighbors required or simply not resample.

        :param X: dataset
        :type X: list
        :param y: lables
        :type y: list
        """
        pass