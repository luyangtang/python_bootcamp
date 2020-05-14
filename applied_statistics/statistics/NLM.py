
# Given data x, y want to estimate beta and sigma

from numbers import Number
import numpy as np
from math import pi, sqrt, exp, log


class SigmaSquare(TypeError):
    message: 'Only non negative values are allowed'


def sigmaSq_check(sigmaSq):

    '''
    Only non negative values are allowed
    '''

    if not isinstance(sigmaSq, Number) or sigmaSq < 0:
        raise SigmaSquare


def numerical_matrix_check(array):

    '''
    np.array
    '''

    if not np.issubdtype(array.dtype, np.number):
        raise TypeError('Only numeric np.arrays are allowed')


def linear_model_dimension_check(y, x, beta = None):
    '''
    beta, y, x should be np.array
    '''

    if y.ndim != 1 or x.ndim != 2 or (y.shape[0] != x.shape[0]):
        raise ValueError('wrong dimension')

    if (np.any(beta)) and ((beta.ndim != 1) or (beta.shape[-1] != x.shape[-1])):
        raise ValueError('wrong dimension')




def list_to_array(*args):
    '''
    Convert python (nested) lists to numerical arrays
    '''

    arrays = []

    for arg in args:
        arg = np.array(arg)
        numerical_matrix_check(arg)

        arrays += [arg]
    
    return arrays



def L(beta, sigmaSq, y, x):

    '''
    Likelihood function

    beta: a list of numbers / a number
    sigma: a non negative numbers
    x: a matrix of numbers, height = height of y, width = width of beta
    '''

    # turn input into numpy matrices
    [beta, y, x] = list_to_array(beta, y, x)
    linear_model_dimension_check(y, x, beta)

    # model property:
    n = y.shape[0]

    # calculate likelihood
    # likelihood = 1

    # for i in range(0, n):
    #     p = exp(- (y[i] - np.dot(x[i], beta)) ** 2 / (2 * sigmaSq)) / sqrt(2 * pi * sigmaSq)
    #     likelihood *= p
    #     print(p, likelihood)

    likelihood= exp(-SS(beta, y, x) / (2 * sigmaSq)) / sqrt(2 * pi * sigmaSq) ** n

    return likelihood

def l(beta, sigmaSq, y, x, keep_const = True):

    '''
    log likelihood function
    '''

    # turn input into numpy matrices
    [beta, y, x] = list_to_array(beta, y, x)
    linear_model_dimension_check(y, x, beta)

    # model property:
    n = y.shape[0]

    
    loglikelihood = (-n * log(sigmaSq)/2 - SS(beta, y, x) / (2 * sigmaSq))

    # the last term is a constant
    if keep_const:
        loglikelihood += - n * log(2 * pi) / 2

    return  loglikelihood
    



def SS(beta, y, x):

    '''
    sum of square
    '''

    # turn input into numpy matrices
    [beta, y, x] = list_to_array(beta, y, x)
    linear_model_dimension_check(y, x, beta)

    ss = 0

    # model property:
    n = y.shape[0]

    for i in range(0, n):

        ss += (y[i] - np.dot(x[i], beta)) ** 2

    return ss
    


def beta_hat(y, x):

    '''
    MLE of beta, maximises the likelihood
    '''

    # turn input into numpy matrices
    [y, x] = list_to_array(y, x)
    linear_model_dimension_check(y, x)

    xt = np.transpose(x)
    xtx = np.matmul(xt, x)

    lin_transform_mat = np.matmul(np.linalg.inv(xtx), xt)

    
    return np.matmul(lin_transform_mat, y)




class NLM(object):

    def __init__(self, y, x):

        # turn input into numpy matrices
        [self.y, self.x] = list_to_array(y, x)
        linear_model_dimension_check(self.y, self.x)

        # model property:
        self.n = self.y.shape[0]

        # get MLE for beta and sigmaSq
        self.__beta_hat = self.__calculate_beta_hat()
        self.__sigmaSq_hat = self.__calculate_sigmaSq_hat()

    

    def __calculate_beta_hat(self):

        return beta_hat(self.y, self.x)


    def __calculate_sigmaSq_hat(self):

        # rss is the minimum value of SS(B)
        self.rss = SS(self.__beta_hat, self.y, self.x)

        return self.rss / self.n

    
    def get_mle(self):
        
        return [self.__beta_hat, self.__sigmaSq_hat]