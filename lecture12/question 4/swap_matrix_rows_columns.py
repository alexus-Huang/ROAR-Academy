import numpy as np

M = np.array([[1,2,3],[4,5,6]])
def swap_rows(array,a,b):
    array[[a,b]] = array[[b,a]]
    print(array)
def swap_columns(array,a,b):
    array[:,[a,b]] = array[:,[b,a]]
    print(array)

swap_rows(M,0,1)
swap_columns(M,0,2)