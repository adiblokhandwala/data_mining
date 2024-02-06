import numpy
from numpy.random import randint
import math 

LENGTH_OF_THE_ARRAY= 10
LOWER_BOUND_OF_VALUES = 0
UPPER_BOUND_OF_VALUES = 100
values = randint(LOWER_BOUND_OF_VALUES,UPPER_BOUND_OF_VALUES,LENGTH_OF_THE_ARRAY)
print("original array: ")
print(values)


#sorting the array
sorted_arr = numpy.sort(values)
print("sorted array: ")
print(sorted_arr)

def equal_width_binning(arr,nbins):
    min = arr[0]
    max = arr[-1]
    in_arr = numpy.zeros((nbins,LENGTH_OF_THE_ARRAY))

    width = math.ceil((max-min)/nbins)
    for i in range(nbins):
        for j in range(len(arr)):
            if(i==nbins-1):
                if(arr[j] >= min + i*width and arr[j]<=max):
                    in_arr[i][j]= arr[j]
            else:
                if(arr[j]>=min + i*width and arr[j]<= (i+1)*width - 1):
                    in_arr[i][j] = arr[j]

    new_arr = [numpy.trim_zeros(arr) for arr in in_arr]


    return new_arr


def equal_frequency_binning(arr,nbins):
    frequency = math.floor(len(arr)/nbins)
    new_arr = [[arr[(frequency*i)+j] for j in range(frequency)] for i in range(math.floor(len(arr)/frequency))]
    return new_arr

def smooth_by_mean(arr_):
    for arr in arr_:
        mean = math.floor(numpy.mean(arr))
        for i in range(len(arr)):
            arr[i] = mean
    return arr_    

def smooth_by_median(arr_):
    for arr in arr_:
        median = math.floor(numpy.median(arr))
        for i in range(len(arr)):
            arr[i] = median
    return arr_ 


def smooth_by_bin_boundaries(arr_):
    for arr in arr_:
        min = arr[0]
        max = arr[-1]
        for i in range(len(arr)):
            if(i<=len(arr)/2):
                arr[i] = min
            else:
                arr[i] = max
    return arr_ 

print("after doing binning to the array: ")
print(equal_width_binning(sorted_arr,10))
print(equal_frequency_binning(sorted_arr,5))
print(smooth_by_mean(equal_width_binning(sorted_arr,3)))
print(smooth_by_median(equal_width_binning(sorted_arr,3)))
print(smooth_by_bin_boundaries(equal_width_binning(sorted_arr,3)))




