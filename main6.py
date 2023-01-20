import math
import numpy as np

def Trapezoidal_Rule():
    points=np.linspace(0,math.pi/2,11)
    w=(math.pi/2)/10.0
    sum=0.0
    for i in range(10):
       sum+=math.sin(points[i])+math.sin(points[i+1])
    sum=sum*(w/2)
    return sum

def Simpsons_Rule():
    points = np.linspace(0, math.pi / 2, 11)
    w=(math.pi/2)/10.0
    sum=0.0
    for i in range(11):
        if (i==0 or i==10):
            sum+=math.sin(points[i])
        elif (i%2==0):
            sum+=math.sin(points[i])*2
        elif (i%2!=0):
            sum+=math.sin(points[i])*4
    sum= sum *w/3
    return sum

print(Trapezoidal_Rule())
print("Error of Trapezoidal Rule is",abs(1-Trapezoidal_Rule()))
print(Simpsons_Rule())
print("Error of Simpson's Rule is",abs(1-Simpsons_Rule()))

