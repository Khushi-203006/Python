'''
-Numpy is short form od Numerical python.
-In 2005, Travis oliphant created Numpy Package.
-Numpy is a package that defines a multi-dimensional
objects and asscociates fast math functions that
operate.
-has function for working in domain of linear algebra,
Fourier Transformationand matrics.
-fundamental package of scientific computing in python.
'''
'''
-------ARRAYS----------
-Collection of items that are stored at contiguous
memory location.
-Conatiner which can hold a fixed number of items, and
these items should be of the same type.
-Combination of arrays saves a lot of the same type.
-Reduce overall size of the code.

#ADVANTAGE OF USING ARRAYS
-Numpy uses much less memory to store data.
-Numpy makes it extremely easy to perform mathematical
operations on it.
-Used for the creation of n-dimensional arrays.
-Finding elements in Numpy array is easy.
'''
'''
import numpy as np
a=np.array([20,30,40])
b=np.array([60,70,80])
print(a)
print(b)
print(a+b)
a=np.array([20,30,40])
b=np.array([60])
print(a)
print(b)
print(a+b)
a=np.array([20,30,40])
b=np.array([6])
print(a)
print(b)
print(a*b)
'''
'''
----ARRAYS V/S LISTS-----
-list cannot directly mathematical operations,while
array can
-array consumes less memory than list
-array is faster than list
-list can store different datatype,while you can't do
that in an array
-list is easier to modify since a list store each
element individually
-easy to add and delete an element than an array does
-list can have different data with different size,
this cannot be done in array
'''
'''
import numpy as np
num= np.array([1,2,3,4,5])
print("Lenght: ",len(num))
print("Sum= ",sum(num))
print("Mean= ",np.mean(num))
print("Minimum=",np.min(num),"Maximum=",np.max(num))
print(num)
for i in range(len(num)):
    print(num[i],end=" ")
'''
'''
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print(arr)
for i in range(len(arr)):
    print(arr[i])
'''
'''
import numpy as np
arr1=np.zeros(10)
for i in range(len(arr1)):
    print(arr1[i],end=" ")
print()
arr1=np.ones(10)
for i in range(len(arr1)):
    print(arr1[i],end=" ")
'''
'''
import numpy as np
arr1= np.arange((10))
for i in range(len(arr1)):
    print(arr1[i],end=" ")
'''
'''
import numpy as np
arr1=np.array([1,2,3,4,5,6,7,8,9,10,12,14])
arr2=arr1.reshape(4,3)
for i in range(len(arr2)):
    print(arr2[i])
'''
'''
import numpy as np
arr1= np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Original Array")
for i in range(len(arr1)):
    print(arr1[i])
print("Transpose of array")
arr2= arr1.transpose()
for i in range(len(arr2)):
    print(arr2[i])
'''
'''
import numpy as np
print("Your 6 digit OTP is: ",end="")
for i in range(0,6):
    otp = np.random.randint(0,9)
    print(otp,end="")
'''





















