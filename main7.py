import numpy as np


def printout_nextresults(ELPEresultsnext,TITCresultsnext):
    print("ELPE stock approximation on my birthday (14/09): \n"
          " Using a 2nd degree polynomial we get: ",ELPEresultsnext[0],"\n",
          "Using a 3rd degree polynomial we get: ",ELPEresultsnext[1],"\n",
          "Using a 4th degree polynomial we get: ",ELPEresultsnext[2],"\n")
    print("TITC stock approximation on my birthday (14/09): \n"
          " Using a 2nd degree polynomial we get: ",TITCresultsnext[0],"\n",
          "Using a 3rd degree polynomial we get: ",TITCresultsnext[1],"\n",
          "Using a 4th degree polynomial we get ",TITCresultsnext[2],"\n")


def printout_fiveresults(ELPEresultsfive, TITCresultsfive):
    print("ELPE stock approximation on the 18th of September: \n"
          " Using a 2nd degree polynomial we get: ", ELPEresultsfive[0], "\n",
          "Using a 3rd degree polynomial we get: ", ELPEresultsfive[1], "\n",
          "Using a 4th degree polynomial we get: ", ELPEresultsfive[2], "\n")
    print("TITC stock approximation on the 18th of September: \n"
          " Using a 2nd degree polynomial we get: ", TITCresultsfive[0], "\n",
          "Using a 3rd degree polynomial we get: ", TITCresultsfive[1], "\n",
          "Using a 4th degree polynomial we get ", TITCresultsfive[2])


def stock_approximations(x,n,flag):
    ELPE=[(0,5.1100),(1,5.2000),(2,5.2400),(3,5.1700),(4,5.1800),(7,5.2500),(8,5.1200),(9,5.1100),(10,5.1100),(11,5.0600)]
    TITC=[(0,11.3800),(1,11.3800),(2,11.2600),(3,11.2400),(4,11.1600),(7,11.1200),(8,10.7800),(9,10.8800),(10,10.8000),(11,10.8200)]
    if (flag==True):
        return Least_Squares(ELPE,x,n)
    else:
        return Least_Squares(TITC,x,n)




def Least_Squares(stockdata,x,n):
    y=np.zeros(10)
    for i in range(len(stockdata)):
        y[i]=stockdata[i][1]
    X = [[0.0 for i in range(n+1)] for j in range(len(stockdata))]
    counter=0
    for i in range(n+1):
        for j in range(len(stockdata)):
            X[j][i]=(stockdata[j][0])**counter
        counter+=1
    a=np.linalg.inv(np.dot(np.transpose(X),X))
    a=np.dot(a,np.transpose(X))
    a=np.dot(a,y)
    result=0
    for i in range(len(a)):
        result+=a[i]*(x**i)
    return result


ELPEresultsnext=[stock_approximations(14,2,True),stock_approximations(14,3,True),stock_approximations(14,4,True)]
TITCresultsnext=[stock_approximations(14,2,False),stock_approximations(14,3,False),stock_approximations(14,4,False)]
ELPEresultsfive=[stock_approximations(18,2,True),stock_approximations(18,3,True),stock_approximations(18,4,True)]
TITCresultsfive=[stock_approximations(18,2,False),stock_approximations(18,3,False),stock_approximations(18,4,False)]

printout_nextresults(ELPEresultsnext,TITCresultsnext)
printout_fiveresults(ELPEresultsfive,TITCresultsfive)