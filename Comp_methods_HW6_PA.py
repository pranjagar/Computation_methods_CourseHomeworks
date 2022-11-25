import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random as rand






# h, w = 50, 50
x,y = 50,50             #initial positions

t = 0                           
conter = 0              # variable to loop in case particle hits the wall

position_list = [[0,0] for i in range(int(1e6))]              # zeros list to update later and store the particle positions in



while t < 1e6:
    r =rand.randint(0,1e5)              # creaating random number
    if r%4 == 0:                        # using modulo 4 to categorize into four arguments
        if x < 101:
            x += 1
            counter = 0                 #
        else:
            counter = 1                 # in case x is already maximum, ocunter beocomes 1
    elif r%4 == 1:
        if x > 0:
            x -= 1
            counter = 0
        else:
            counter = 1
    elif r%4 == 2:
        if y < 101:
            y += 1
            counter = 0
        else:
            counter = 1
    elif r%4 == 3:
        if y > 0:
            y -= 1
            counter = 0
        else:
            counter = 1
    if counter ==0:                                     # if counter is zero its good. if it's 1, nothing is added to t, thus loop repeats
        position_list[t] = [x,y]                        # updating particle position
        t += 1                                      
    

fig = plt.figure(figsize=(10,10))
ax = plt.axes(xlim=(0, 101), ylim=(0, 101))
earth = plt.Circle((20, 20), .5, fc='b')

def init():
    earth.center = (50,50)
    ax.add_patch(earth)
    return earth,

def animate(i):
    x = position_list[i][0]
    y = position_list[i][1]
    earth.center = (x, y)
    return earth,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames= 1000000, interval=20, blit=True)
plt.show()