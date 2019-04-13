# making the unicycle model
import numpy as np
import matplotlib.pyplot as plt

def unicycle_model(xVectorCurrent,v,w):
    # implement the unicycle model
    tht = xVectorCurrent[2]
    xVectorNext = xVectorCurrent + np.matrix([[np.cos(tht), 0],[np.sin(tht), 0],[0,1]]) * np.matrix([[v],[w]])
    return xVectorNext


def unicycle_test():
    A=[]
    xVectorStart = np.matrix([[0],[0],[np.pi/4]])
    v = [0,1,2,3,4,5]
    w = [1,-1,1,-1,1,-1]
    for vs,ws in zip(v,w):
        A.append(unicycle_model(xVectorStart,vs,ws))
    return A
if __name__ == "__main__":
    Z = unicycle_test()
    print(Z)
    plt.plot(Z[0][:],Z[1][:])
    plt.show()
