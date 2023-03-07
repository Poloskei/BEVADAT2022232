
import numpy as np








def create_array(size:tuple=(2,2))->list:
    return np.zeros(size,dtype=int)





def set_one(inputArray:np.array)->np.array:
    np.fill_diagonal(inputArray,1)
    return inputArray





def do_transpose(inputArray:np.array)->np.array:
    return np.transpose(inputArray)





def round_array(inputArray:np.array,roundTo:int=2)->np.array:
    return np.around(inputArray,roundTo)





def bool_array(inputArray:np.array)->np.array:
    return np.array(inputArray,dtype=bool)





def invert_bool_array(inputArray:np.array)->np.array:
    return np.invert(
        np.array(inputArray,dtype=bool))




def flatten(inputArray:np.array)->np.array:
    return np.ndarray.flatten(inputArray)





