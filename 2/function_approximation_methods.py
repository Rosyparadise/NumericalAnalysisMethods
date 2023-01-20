import math
import matplotlib.pyplot as plt
import numpy as np


def Lagrange_Polynomial(sinv,x):

    y=0
    Lagrangians=[]

    for i in range(len(sinv)-1):
        sum1 = 1
        sum2 = 1
        for j in range(len(sinv)-1):
            if (i==j):
                continue

            else:
                sum1*=(x-sinv[j][0])
                sum2*=(sinv[i][0]-sinv[j][0])

        Lagrangians.append(sinv[i][1]*(float(sum1)/sum2))

    for i in range(len(Lagrangians)):
        y+=Lagrangians[i]
    return y


def Least_Squares(sinv,x):
    y=np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
    for i in range(len(sinv)):
        y[i]=sinv[i][1]


    X=np.array([[0.0,0.0,0.0,0.0,0.0,0.0],
               [0.0,0.0,0.0,0.0,0.0,0.0],
               [0.0,0.0,0.0,0.0,0.0,0.0],
               [0.0,0.0,0.0,0.0,0.0,0.0],
               [0.0,0.0,0.0,0.0,0.0,0.0],
               [0.0,0.0,0.0,0.0,0.0,0.0],
               [0.0,0.0,0.0,0.0,0.0,0.0],
               [0.0,0.0,0.0,0.0,0.0,0.0],
               [0.0,0.0,0.0,0.0,0.0,0.0],
               [0.0,0.0,0.0,0.0,0.0,0.0]])
    counter=0
    for i in range(6):
        for j in range(len(sinv)):
            X[j][i]=(sinv[j][0])**counter
        counter+=1
    a=np.linalg.inv(np.dot(np.transpose(X),X))
    a=np.dot(a,np.transpose(X))
    a=np.dot(a,y)
    result=0
    for i in range(len(a)):
        result+=a[i]*(x**i)
    return result



def Natural_Cubic_Splines(sinv, x):
    w=np.zeros(9)
    h=np.zeros(9)
    for i in range(len(sinv)-1):
        w[i]=sinv[i+1][0]-sinv[i][0]
        h[i]=(sinv[i+1][1]-sinv[i][1])/w[i]
    fder2=np.zeros(10)
    for i in range(0,len(sinv)-2):
        fder2[i+1]=3*(h[i+1]-h[i])/(w[i+1]+w[i])
    A=[]
    B=[]
    C=[]
    D=[]
    for i in range(len(sinv)-1):
        A.append((fder2[i+1]-fder2[i])/(6.0*w[i]))
        B.append(fder2[i]/2.0)
        C.append(h[i]-w[i]*(fder2[i+1]+2*fder2[i])/6.0)
        D.append(sinv[i][1])

    if (x>=-math.pi and x<-2.1):
        result=D[0]+C[0]*(x+math.pi)+B[0]*(x+math.pi)**2+A[0]*(x+math.pi)**3
    elif(x>=-2.1 and x<-1.4):
        result=D[1]+C[1]*(x+2.1)+B[1]*(x+2.1)**2+A[1]*(x+2.1)**3
    elif(x>=-1.4 and x<-0.3):
        result=D[2]+C[2]*(x+1.4)+B[2]*(x+1.4)**2+A[2]*(x+1.4)**3
    elif (x >= -0.3 and x < 0.0):
        result = D[3]+C[3]*(x+0.3)+B[3]*(x+0.3)**2+A[3]*(x+0.3)**3
    elif (x >= 0.0 and x < 0.7):
        result = D[4] + C[4] * (x) + B[4] * (x) ** 2 + A[4] * (x) ** 3
    elif (x >= 0.7 and x < 1.5):
        result = D[5] + C[5] * (x-0.7) + B[5] * (x-0.7) ** 2 + A[5] * (x-0.7) ** 3
    elif (x >= 1.5 and x < 2.2):
        result = D[6] + C[6] * (x-1.5) + B[6] * (x-1.5) ** 2 + A[6] * (x-1.5) ** 3
    elif (x >= 2.2 and x < 2.9):
        result = D[7] + C[7] * (x-2.2) + B[7] * (x-2.2) ** 2 + A[7] * (x-2.2) ** 3
    elif ( x >= 2.9 and x <= math.pi):
        result = D[8] + C[8] * (x-2.9) + B[8] * (x-2.9) ** 2 + A[8] * (x-2.9) ** 3
    return result



sin_values3 = [(-math.pi,math.sin(-math.pi)),(-2.1,math.sin(-2.1)),(-1.4,math.sin(-1.4)),(-0.3,math.sin(-0.3)),(0.0,math.sin(0.0)),(0.7,math.sin(0.7)),(1.5,math.sin(1.5)),(2.2,math.sin(2.2)),(2.9,math.sin(2.9)),(math.pi,math.sin(math.pi))]




points=np.linspace(-math.pi,math.pi,200)
lagrange= []
leastsquares= []
cubicsplines=[]
for i in range(200):
    lagrange.append(math.sin(points[i])-Lagrange_Polynomial(sin_values3,points[i]))
    leastsquares.append(math.sin(points[i])-Least_Squares(sin_values3,points[i]))
    cubicsplines.append(math.sin(points[i])-Natural_Cubic_Splines(sin_values3,points[i]))

plt.plot(points, leastsquares, label="least squares error")
plt.plot(points, lagrange, label="lagrange error")
plt.plot(points, cubicsplines, label="cubic splines error")
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.legend()
plt.show()

mean_error_lagrange=0
mean_error_splines=0
mean_error_least_squares=0
for i in range(200):
    mean_error_lagrange+=abs(lagrange[i])
    mean_error_splines+=abs(cubicsplines[i])
    mean_error_least_squares+=abs(leastsquares[i])

mean_error_lagrange/=200.0
mean_error_splines/=200.0
mean_error_least_squares/=200.0

print("mean error of Least squares:",mean_error_least_squares)
print("mean error of Splines:",mean_error_splines)
print("mean error of Lagrange:",mean_error_lagrange)





















