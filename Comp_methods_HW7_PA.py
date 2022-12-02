import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

N = int(1e6)                     # numebr of points
Z = np.linspace(0,1,N+1)
qz = [z**2 for z in Z]               # x = z^2  is the transformed funciton

W = 2 # integral of w(x) function from 0 to 1

def g(x):                  # the weighted function
    return (1)/(1+np.exp(x))

# formula : I = (1/N)*Sum( g(x_i))*W
I = (1/N)*W*np.sum([g(z) for z in qz])
print(I)
