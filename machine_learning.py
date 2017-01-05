__author__ = 'Shubham'
import numpy as np
import csv
from sklearn import ensemble
import math

X=np.zeros(())
Y=np.zeros(())
X2=np.zeros(())
Y2=np.zeros(())
Yfinal=np.zeros(())
def readdata():
    global X,Y,X2,Y2

    X1=np.genfromtxt("userfinal.csv",delimiter=',')

    X=X1[:100,1:-1]
    Y=X1[:100,-1:]
    Y=Y.flatten()

    X2=X1[100:,1:-1]
    Y2=X1[100:,-1:]
    Y2=Y2.flatten()
    #print Y
from sklearn import svm
def gradient_descent_2(alpha, x, y, numIterations):
    m = x.shape[0] # number of samples
    theta = np.ones(7)
    x_transpose = x.transpose()
    for iter in range(0, numIterations):
        hypothesis = np.dot(x, theta)
        loss = hypothesis - y
        J = np.sum(loss ** 2) / (2 * m)  # cost
        print "iter %s | J: %.3f" % (iter, J)
        gradient = np.dot(x_transpose, loss) / m
        theta = theta - alpha * gradient  # update
    return theta
def fitmodel():
    global X2,Y2
    global Yfinal
    rf=ensemble.RandomForestRegressor()
    rf=svm.SVR()
    rf.fit(X,Y)

    Yfinal=rf.predict(X2)

def fitgradientdiscent():
    global X2,Y2
    global Yfinal
    #rf=ensemble.RandomForestRegressor()
    #rf=svm.SVR()
    X1=X/(1+X.max(axis=0))
    m, n = np.shape(X1)
    X1 = np.c_[ np.ones(m), X1] # insert column
    alpha = 0.01 # learning rate
    theta = gradient_descent_2(alpha, X1, Y, 2000)
    #rf.fit(X,Y)
    m, n = np.shape(X2)
    X2= np.c_[ np.ones(m), X2]
    X2=X2/(1+X2.max(axis=0))
    Yfinal=np.dot(X2,theta)
    #Yfinal=rf.predict(X2)


def error():
    e=0
    i=0
    while i<len(Y2):
        e+=(Yfinal[i]-Y2[i])**2
        i+=1
    e=math.sqrt(e)/len(Y2)
    print e


if __name__ == '__main__':
    readdata()
    fitmodel()
    #fitgradientdiscent()
    error()