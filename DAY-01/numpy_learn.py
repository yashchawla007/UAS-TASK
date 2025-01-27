import numpy as np

myArr = np.array([[3, 5, 7], [2, 4, 6]])
print(myArr)
print(myArr.dtype) #& returns the data type of array, it can be int, float, object etc.
print(myArr.shape) #& returns no. of rows and columns

zeroArr = np.zeros((3, 5))

print(zeroArr)
print(zeroArr.dtype)
print(zeroArr.shape)

rng = np.arange(15)
print(rng)

lspace = np.linspace(1, 50, 10) #& give equally spaced elements
print(lspace)

emp = np.empty((2,3))
print(emp)

emp_like = np.empty_like(lspace)
print(emp_like)

ide = np.identity(5)
print(ide)

arr = np.arange(33)
print(arr)
arr = arr.reshape(3, 11)
print(arr)
arr = arr.ravel()
print(arr)

x = [[1, 2, 3], [4, 5, 6], [7, 1, 0]]
ar = np.array(x)
print(ar)
print(ar.sum(axis=0)) #& axis-0 (↓)
print(ar.sum(axis=1)) #& axis-1 (→)
print(ar.T) #& transpose
print(ar.flat)
print(ar.ndim) #& number of dimensions
print(ar.size) #& number of elements
print(ar.nbytes) #& total bytes consumed

for items in ar.flat:
    print(items)

oneD = np.array([1, 2, 4, 343, 3, 9, 0])
print(oneD.argmax()) #& give index of max element
print(oneD.argmin()) #& give index of min element
print(oneD.argsort()) #& give array of index of sorted array

y = [[1, 2, 3], [4, 5, 6], [7, 1, 0]]
twoD = np.array(y)
print(twoD.argmax()) #& first arrange linearly then give index of max element
print(twoD.argmin()) #& first arrange linearly then give index of min element
print(twoD.argsort()) #& give array of index of sorted array
print(f"argmax(axis=0): {twoD.argmax(axis=0)}")
print(f"argmax(axis=1): {twoD.argmax(axis=1)}")
print(f"argmin(axis=0): {twoD.argmin(axis=0)}")
print(f"argmin(axis=1): {twoD.argmin(axis=1)}")
print(f"argsort(axis=0): {twoD.argsort(axis=0)}")
print(f"argsort(axis=1): {twoD.argsort(axis=1)}")

#--------------- MATRIX OPERATIONS ---------------#

mt1 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 1, 0]])

mt2 = np.array([[6, 7, 3],
                [1, 2, 0],
                [3, 6, 9]])

print(f"mt1 + mt2: \n{mt1 + mt2}")
print(f"mt1 + mt2: \n{mt1 - mt2}")
print(f"mt1 + mt2: \n{mt1 * mt2}")
# print(f"mt1 + mt2: \n{mt1 / mt2}")
# print(f"mt1 + mt2: \n{mt1 % mt2}")
print(f"sqrt(mt1): \n{np.sqrt(mt1)}")
print(f"where(mt1 > 5): \n{np.where(mt1 > 5)}")
print(f"count non zero: \n{np.count_nonzero(mt1)}")
print(f"non zero: \n{np.nonzero(mt1)}")
