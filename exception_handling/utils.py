def useless_sum(*args):

    '''
    Sum up all positional arguments
    '''

    sum = 0

    for arg in args:
        sum += arg

    return sum