import numpy as np

def column_swap(input_array:np.array)->np.array:
    temp=np.copy(input_array[:,0])
    input_array[:,0] = input_array[:,1]
    input_array[:,1] = temp
    return input_array

def compate_two_array(input_array1:np.array, input_array2:np.array)->np.array:
    return np.where(np.equal(input_array1, input_array2))
