import unittest



from statistics.MLE import *
import numpy as np


class TestMLE(unittest.TestCase):




    def test_linear_model_dimension_check(self):

        beta = np.array([0, 1, 2])
        y = np.array([1, 2, 3, 4, 5])
        x = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15]])

        linear_model_dimension_check(beta, y, x)


        beta = np.array([0, 1])
        y = np.array([1, 2, 3, 4, 5])
        x = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15]])

        self.assertRaises(
            ValueError,
            linear_model_dimension_check,
            beta, y, x
        )


        beta = np.array([0, 1, 2])
        y = np.array([1, 2, 3, 4, 5])
        x = np.array([[4,5,6], [7,8,9], [10,11,12], [13,14,15]])

        self.assertRaises(
            ValueError,
            linear_model_dimension_check,
            beta, y, x
        )



    def test_list_num_sanity_check(self):

        beta = [0, 1, 2]
        y = [1, 2, 3, 4, 5]
        x = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15]]
        sigmaSq = 3
    
        L(beta, sigmaSq, y, x)

        beta = [0, 1, 2]
        y = [1, 2, 3, 4, 5]
        x = [['a',2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15]]
        sigmaSq = 3
        self.assertRaises(
            TypeError,
            L,
            beta, sigmaSq, y, x
        )


    
    def test_list_to_array(self):

        beta = [0, 1, 2]
        y = [1, 2, 3, 4, 5]
        x = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15]]


        res = list_to_array(beta, y, x)
        for i, v in enumerate([beta, y, x]): 
            self.assertTrue(
                np.all(np.equal(
                    res[i],
                    np.array(v)
                )
            ))
            


    
    def test_numerical_matrix_check(self):

        self.assertRaises(
            TypeError,
            numerical_matrix_check,
            np.array([['a',2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15]])
        )

        numerical_matrix_check(np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15]]))
        numerical_matrix_check(np.array([1,2,3]))
        numerical_matrix_check(np.array(1))



    def test_sigmaSq_check(self):

        self.assertRaises(SigmaSquare, sigmaSq_check, -1)
        self.assertRaises(SigmaSquare, sigmaSq_check, 'a')
        sigmaSq_check(1)



    
    def test_L(self):

        beta = [0, 1, 2]
        y = [1, 2, 3, 4, 5]
        x = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15]]
        sigmaSq = 3

        likelihood = L(beta, sigmaSq, y, x)

        self.assertTrue(likelihood != 1)
        self.assertTrue(likelihood > 0)