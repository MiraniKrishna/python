import array
a=array.array('i',[10,20,30,40,50])
for i in range(5):
    print(a[i])
#==============================================
import array as ar
b=ar.array('i',[10,20,30,40,50])
for i in range(5):
    print(b[i])
#==============================================
from array import *
c=array('i',[10,20,30,40,50])
for i in range(5):
    print(c[i])
#==============================================
#unicode
import array
d=array.array('u',['a','b','c','d','e'])
for i in range(5):
    print(d[i])
#==============================================
#float
import array
e=array.array('f',[10.5,20.5,30.5,40.5,50.5])
for i in range(5):
    print(e[i])
#==============================================
#slicing
print(a[1:4:2])
print(b[1::2])
print(c[4:])
print(d[::])
print(e[::2])
print(a[1::])












