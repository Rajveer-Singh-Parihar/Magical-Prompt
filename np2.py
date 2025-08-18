# SLICING OF NUMPY ARRAYS
# 1 DIMENSIONAL ARRAY 
import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5]) # runs in n-1 
print("\n")

b = np.array([1,2,3,4,5,6,7])
print(b[::2]) # skip one one sequence
print("\n")

# SLICING IN 2D ARRAY
a=np.array([[10,20,30,40,50],[60,70,80,90,100]])
print(a[1,1:4]) # 70 ,80,90
print(a[0,0:4]) # 10 ,20 ,30 ,40
print("\n")

# CHECKING THE DATA TYPE OF AN ARRAY
c = np.array([1,2,3,4,5])
print((c.dtype)) # gives the type of an array
d = np.array(['animals','bat','cat'])
print(d.dtype)
print("\n")

#Creating array with defined datatype
arr = np.array([1,2,3,4],dtype='S')
print(arr)
print(arr.dtype)
print("\n")

#  creating an array with 4bytes integer
arr=np.array([1,2,3,4],dtype="i4")
print(arr)
print(arr.dtype)
print("\n")

# NUMPY ARRAY SHAPE - the shape of an array is the number of elements in each dimension.
# printing the shape of 2d array
r = np.array([[1,2,3,4],[5,6,7,8]])
print(r.shape) # (2,4) - 2d array with 4 elements
print("\n")

r = np.array([[[1,2,3,4],[5,6,7,8],[10,20,30,40]]])
print(r.shape) # (1,3,4) 
print("\n")

# JOINING NUMPY ARRAY
arr1 = np.array([1,2,3,4])
arr2=np.array([6,7,8,9])
arr = np.concatenate((arr1,arr2))
print(arr) # [1,2,3,4,6,7,8,9]
print("\n")

# JOINING 2D ARRAY - there is mainly two axis
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])
arr =np.concatenate((arr1,arr2),axis=1) # according to rows
print(arr)
arr =np.concatenate((arr1,arr2),axis=0) # according to columns
print(arr)
print("\n")

# SPLITING NUMPY ARRAY - todna
# spliting array in three parts
arr =np.array([1,2,3,4,5,6])
newarr = np.array_split(arr,3)
print(newarr)
print("\n")

#SPLITTING ARRAY IN 4 PARTS
arr =np.array([1,2,3,4,5,6])
newarr = np.array_split(arr,4)
print(newarr)
print("\n")

# RAVEL AND FLATTEN - Converts Multi - Dimensional Array into 1d array
m = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(m)
n=m.ravel()
print(n)
print("now its become",n.ndim) # return 1d array

m = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(m)
n=m.flatten()
print(n)
print("now its become",n.ndim) # 1d array
print("\n")

c =np.array([[[1,2,3],[34,56,78]],[[354,66,43],[46,46,33]]])
print(c)
d=c.ravel() # we can use flatten
print(d)
print("\n")

#UNIQUE FUNCTION
k = np.array([12,1,4,6,7,8,55,45,23,21,1,32,33,21])
print(k)
x=np.unique(k)
print(x)
print("\n")
k = np.array([12,1,4,6,7,8,55,45,23,21,1,32,33,21])
print(k)
x=np.unique(k,return_index= True,return_counts=True) # returns index
print(x)

# DELETE
a = np.array([12,23,45,56])
d =np.delete(a,[1])
print(d)
print("\n")
 
x=np.array([[2,7,9,6,8],[3,5,6,7,8],[50,0,65,6,7]])
print(x)
m = np.delete(x,1,axis=0) # column - 1
print(m)