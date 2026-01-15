from math import pi
from math import sin
from math import cos
from math import ceil

def areaform(a,b,c):  
    s = (a + b + c) / 2   
    area = (s*(s-a) * (s-b)*(s-c)) ** 0.5        
    return area

def distance3d(x1,y1,z1,x2,y2,z2):    
    a=(x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
    dist = a ** 0.5  
    return dist 

def areatriangle3d(x1,y1,z1,x2,y2,z2,x3,y3,z3):  
    a = distance3d(x1,y1,z1,x2,y2,z2)  
    b = distance3d(x2,y2,z2,x3,y3,z3)  
    c = distance3d(x3,y3,z3,x1,y1,z1)
    area = areaform(a,b,c) 
    return area


def floatrange(start, stop, step):
    n = int(ceil((stop - start) / step))
    return (start + i*step for i in range(n))

max = 0
maxa = 0
for i in floatrange(0,2*pi,0.0001):
    area = areatriangle3d(2, cos(i),sin(i), sin(i), 2, cos(i), cos(i), sin(i), 2)
    if area > maxa:
       max = i
       maxa = area

print(max,maxa)
print(max*maxa)
print(2, cos(max),sin(max), sin(max), 2, cos(max), cos(max), sin(max), 2)