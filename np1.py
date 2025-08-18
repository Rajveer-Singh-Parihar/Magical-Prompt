import numpy as np
arr = np.array([1,24,56,66])
print(arr)
print("\n")

# 2D ARRRAY
arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]]) # same number elemnts - we can also take floating point number
print(arr2)
print(np.sum(arr2)) # 1
print(arr2[0,:]) # zero row all element
print(arr2[1,:]) # first row all element
print(arr2.ndim)
print("\n")

# CREATING 3D ARRAY - array with 2-d array(metrices) as its elements is called 3d array.
arr3 = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr3)
print(arr3.ndim)
print("\n")

#CREATING 5D ARRA
arr5 = np.array([1,2,3,4],ndmin=5)
print(arr5)
print(arr5.ndim)
print("\n")

# NUMPY ARRAY INDEXING - ARRAY INDEXING IS SAME AS ACCESSING ARRAY ELEMENTS.
a = np.array([1,2,3,4]) # indexing start from zero
print(a[0])
print(a[0:2]) # 1,2 - not 3
print("\n")

#Basic Question
m =np.array([41,2,3,45,67,54,77,54,677,44,64,33])
print("the secound elements is",m[2])
print("the secound elements is",m[5])
print("the secound elements is",m[7])
print("The Sum of element is",m[2]+m[5]+m[7])
print("\n")

#INDEXING IN 2D ARRAY
b = np.array([[1,2,3,4],[5,6,7,8]]) # here inside array is for row 0 and 1 - here value is one 
print('Secound element in first row',b[0,1])
print("\n")

c = np.array([[1,2,3,4],[5,6,7,8]]) # here inside array is for row 0 and 1 - here value is four
print('Fourth element in first row',c[0,3])
print("\n")

d = np.array([[1,2,3,4,10,30],[5,6,7,8,20,40]]) # here inside array is for row 0 and 1 - here value is twenty 
print('Fifth element in first row',d[1,4])
print("\n")

# SOME BASIC SHORT OF QUESTION
r = np.array([[10,20,30,40,50],[60,70,80,90,100]])
print("first element of 1st row",r[0,1])
print("last Element of secound row",r[1,4])
print("Sum of Array",r[0,1]+r[1,4])
print("\n")

#ACCESSING THE THREE DIMENSION ARRAY
j= np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) #6
print(j[0,1,2])
print("\n")

j= np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) #12
print(j[1,1,2])
print("\n")

j= np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) #8
print(j[1,0,1]) 
print("\n")

j= np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) #3
print(j[0,0,2])
print("\n")







