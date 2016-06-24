# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:23:56 2015

@author: esufan
"""
import numpy as np

# CMBAS Class *****************************************************************
class Cmbas(object):
    """ Class containing all methods for calcule of covariance matrix. """

    def __init__(self):
        """ Cmbas constructor. Initialize new list of matrices.
            parameters: 
            - """
        self.matrix_list = []


    def add_matrix_to_list(self, matrix):
        """ Function to apend new matrix to the list "matrix_list" 
            parameters: 
            - matrix: numpy array. """
        self.matrix_list.append(matrix)
        print "Added new matrix to the list \n" 


    def calc_covariance(self):
        """ Function to calculate covariance in all matrices received as input.
            parameters: 
            - matrix_list: list of matrices to calculate covariance.
            returns:
            - covariance matrix associated. """

        matrix_stack = np.dstack(self.matrix_list) # Stack into 3D array. FIXME: check if posible with np.reshape of the previous list.
        cmbas        = 0.                          # Covariance for matrix.  

        print  "matrix_stack: \n", matrix_stack                 


        # Obtain number of rows and columns to parametrized reshape.
        nrows    = matrix_stack.shape[0]*matrix_stack.shape[1]
        ncolumns = matrix_stack.shape[2]

        # Obtain number of elements to calculate covarianze.
        nelems   = matrix_stack.size

        # Reshape into 2D matrix.        
        matrix_stack_2d = np.reshape( matrix_stack, (nrows, ncolumns))
        
        # Calculate covariance.
        for i in matrix_stack_2d:        
            icT    = i.conj().T        # Get conjutate transpose.
            cmbas += np.dot(i, icT)    # Get covariance.

        # Get final value of covariance.
        cmbas = cmbas/nelems   
        
        print "Resultan cmbas: ", cmbas
        return cmbas





# Main for easy test **********************************************************
def main():
    
    # Matrices for test.
    m1 = np.array([
                  ( 1. + 1.j  , 2. + 2.j  , 3. + 3.j ),
                  ( 4. + 4.j  , 5. + 5.j  , 6. + 6.j ),
                  ( 7. + 7.j  , 8. + 8.j  , 9. + 9.j )
                  ], dtype='complex64')
        
    m2 = np.array([
                  ( 11. + 11.j, 12. + 12.j, 13. + 13.j ),
                  ( 14. + 14.j, 15. + 15.j, 16. + 16.j ),
                  ( 17. + 17.j, 18. + 18.j, 19. + 19.j )
                  ], dtype='complex64')
              
    m3 = np.array([
                  ( 21. + 21.j, 22. + 22.j, 23. + 23.j ),
                  ( 24. + 24.j, 25. + 25.j, 26. + 26.j ),
                  ( 27. + 27.j, 28. + 28.j, 29. + 29.j )
                  ], dtype='complex64')
                  

    m4 = np.array([
                  ( 1. + 1.j, 1. + 1.j, 1. + 1.j ),
                  ( 1. + 1.j, 1. + 1.j, 1. + 1.j ),
                  ( 1. + 1.j, 1. + 1.j, 1. + 1.j )
                  ], dtype='complex64')


    m5 = np.array([
                  ( 0. + 0.j, 0. + 0.j, 0. + 0.j ),
                  ( 0. + 0.j, 0. + 0.j, 0. + 0.j ),
                  ( 0. + 0.j, 0. + 0.j, 0. + 0.j )
                  ], dtype='complex64')
                  
                  
    m6 = np.array([
                  ( 1. + 0.j, 1. + 0.j, 1. + 0.j ),
                  ( 1. + 0.j, 1. + 0.j, 1. + 0.j ),
                  ( 1. + 0.j, 1. + 0.j, 1. + 0.j )
                  ], dtype='complex64')

    m7 = np.array([
                  ( 1. + 1.j, 1. + 1.j ),
                  ( 1. + 1.j, 1. + 1.j ),
                  ( 1. + 1.j, 1. + 1.j )
                  ], dtype='complex64' )

                  
    m8 = np.array([
                  ( 1. + 0.j, 1. + 0.j ),
                  ( 1. + 0.j, 1. + 0.j ),
                  ( 1. + 0.j, 1. + 0.j )
                  ], dtype='complex64' )


    # Create object to calculate covariance matrix.    
    cmbas = Cmbas()
    cmbas.add_matrix_to_list(m7)
    cmbas.add_matrix_to_list(m8)
#    cmbas.add_matrix_to_list(m3)

    cmbas.calc_covariance()


if __name__ == "__main__":
    main()
       