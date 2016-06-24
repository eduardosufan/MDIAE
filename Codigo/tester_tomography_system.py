# -*- coding: utf-8 -*-
"""
Created on 24/02/2016

@author: esufan
"""
import input_data_handler as idh
import cmbas
import numpy as np  # @UnusedImport


def main():
    
    # Create matrices for calculation (3 pixels each)
    #m1 = idh.create_ones_and_zeros_matrix(3, 3, 'float32')
    #m2 = idh.create_ones_and_zeros_matrix(3, 3, 'float32')
    
    
    m1 = idh.create_simple_matrix()
    m2 = idh.create_simple_matrix()
    ocmbas = cmbas.Cmbas()
    #matrices = np.concatenate(m1,m2)

    matrices = [m1, m2]

    #print matrices.shape
            
    ocmbas.calc_covariance(matrices)
    
    
#**************************************************************************************************************************************************
if __name__ == "__main__":
    main()

