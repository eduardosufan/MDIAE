# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 14:52:08 2015

@author: usuario01
"""
import numpy as np
import itertools as it


def create_ones_and_zeros_matrix(n_rows, n_columns, datatype='float32'):
    """ Create a matrix with ones in pair rows, and zeros in odd rows
        parameters:
        n_rows: number of rows of the matrix
        n_columns: number of colums of the matrix
        datatype: data type of matrix elements
    """
    # Create auxiliar matrix and vector with ones.
    aux_matrix      = np.zeros((n_rows, n_columns), dtype=datatype)
    aux_ones_vector = np.ones((1,n_columns), dtype=datatype)     

    # Fill matrix with ones in pair rows    
    for i,e in enumerate(aux_matrix):
        if i%2==0:
            aux_matrix[i][:]=aux_ones_vector
            
    #print aux_matrix
    #print type(aux_matrix[1][1])
            
    return aux_matrix
    
    
def create_simple_matrix():
    
    #m1 = np.zeros((3, 3), dtype='float32')
    #m2 = np.zeros((3, 3), dtype='float32')
    #m3 = np.ones((3, 3), dtype='float32')
    m3 = np.array([
             [ 1. + 1.j, 1. + 1.j, 1. + 1.j ],
             [ 1. + 1.j, 1. + 1.j, 1. + 1.j ],
             [ 1. + 1.j, 1. + 1.j, 1. + 1.j ]
             ], dtype='complex64')
        
    m1 = np.array([
             ( 1. + 1.j, 2. + 2.j, 3. + 3.j ),
             ( 4. + 4.j, 5. + 5.j, 6. + 6.j ),
             ( 7. + 7.j, 8. + 8.j, 9. + 9.j )
             ], dtype='complex64')
        
    m2 = np.array([
             ( 11. + 11.j, 12. + 12.j, 13. + 13.j ),
             ( 14. + 14.j, 15. + 15.j, 16. + 16.j ),
             ( 17. + 17.j, 18. + 18.j, 19. + 19.j )
             ], dtype='complex64')
    
    #N       = 3     
    #N_array = range(N)
    
#    stackOfImages = np.array((m1, m2)) # Iterate over these matrix if many more.
#    stackOfImages = np.array((stackOfImages, m3))
    stackOfImages = np.array((m1, m2, m3)) # Iterate over these matrix if many more.
    
    #concatenatematrix(m1)
    
    print stackOfImages
    print stackOfImages.shape
    print type(stackOfImages)
    

    # Two fors to extract the vector from 3D Matrix.  
    for fila in range(m1.shape[0]):
        for columna in range(m1.shape[1]):
            redData = stackOfImages[:, fila, columna] 
            print redData
            print "\n" 



    
def main():
    
    # Test for creation of matrix
    #create_ones_and_zeros_matrix(10, 10, 'float32')    
    create_simple_matrix()
    #calculate_cov()
    

    
    
    
    
#**************************************************************************************************************************************************
if __name__ == "__main__":
    main()