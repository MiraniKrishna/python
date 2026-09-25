from numpy import *
#single dimentional
a=array([1,2,3])
print("Single dimentional : ",a)

#two dimentional
b=array([[1,2,3],[4,5,6]])
print("Two dimentional : ",b)

#multi dimentional
c=array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("Multi dimentional : ",c)

print("ndim attribute")
print("a ndim : ",a.ndim)
print("b ndim : ",b.ndim)
print("c ndim : ",c.ndim)

print("shape attribute")
print("a shape : ",a.shape)
print("b shape : ",b.shape)
print("c shape : ",c.shape)

print("size attribute")
print("a size : ",a.size)
print("b size : ",b.size)
print("c size : ",c.size)

print("itemsize attribute")
print("a itemsize : ",a.itemsize)
print("b itemsize : ",b.itemsize)
print("c itemsize : ",c.itemsize)

print("dtype attribute")
print("a dtype : ",a.dtype)
print("b dtype : ",b.dtype)
print("c dtype : ",c.dtype)

print("nbytes attribute")
print("a nbytes : ",a.nbytes)
print("b nbytes : ",b.nbytes)
print("c nbytes : ",c.nbytes)


