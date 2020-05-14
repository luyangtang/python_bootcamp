
# Given data x, y want to estimate beta and sigma

from numbers import Number
import numpy as np
from math import pi, sqrt, exp


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


def linear_model_dimension_check(beta, y, x):
    '''
    beta, y, x should be np.array
    '''

    if (y.ndim != 1) or (beta.ndim != 1) or (x.ndim != 2):
        raise ValueError('wrong dimension')

    if (y.shape[0] != x.shape[0]) or (beta.shape[-1] != x.shape[-1]):
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

    # model property:
    n = y.shape[0]

    # calculate likelihood
    likelihood = 1

    for i in range(0, n):

        p = exp(- (y[i] - np.dot(x[i], beta)) ** 2 / (2 * sigmaSq)) / sqrt(2 * pi * sigmaSq)
        likelihood *= p

    return likelihood