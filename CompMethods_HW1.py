#import math as m
import numpy as n
import matplotlib.pyplot as plt

def theta_variable_list(start, stop):
    kkk = n.linspace(start,stop, int((stop-start)*50))
    return kkk

theta = theta_variable_list(0,2*n.pi)
x = 2*n.cos(theta)+n.cos(2*theta)
y = 2*n.sin(theta)-n.sin(2*theta)
"""plt.plot(x,y)
plt.title("Deltoid Curve")
plt.xlabel("x")
plt.ylabel("y")
#plt.show()
"""
#print(theta_variable_list(0,10*n.pi))


####HW 1 problem (b)

theta1 = theta_variable_list(0, 10 * n.pi)       # created list of numbers using linspace, called theta

r = (theta1) ** 2                              # change function here

x1 = r*n.cos(theta1)                          # change the list variables
y1 = r*n.sin(theta1)                         # change the list variables
"""
plt.plot(x1,y1)
plt.xlabel("x")
plt.title(r' $f(\theta) = {\theta}^2$')
plt.ylabel("y")
#plt.show()
"""

############# prob # (c)

theta2 = theta_variable_list(0, 24 * n.pi)       # created list of numbers using linspace, called theta
theta2by12 = [x/12 for x in theta2]
#print(theta2by12)
r2 = n.exp(n.cos(theta2)) - 2 * n.cos(4 * theta2) + n.sin(theta2by12)** 5                              # change function here
#print(r)

x2 = r2 * n.cos(theta2)                          # change the list variables
y2 = r2 * n.sin(theta2)                         # change the list variables
"""
plt.plot(x2,y2)
plt.title("Fey function ")
plt.xlabel("x")
plt.ylabel("y")
#plt.show()
"""

fig,axes=plt.subplots(1,3,figsize=(16, 5))
ax1 = axes[0].plot(x,y)
ax2 = axes[1].plot(x1,y1)
ax3= axes[2].plot(x2,y2)
axes[0].set_title('Deltoid Curve')
axes[1].set_title('Galilean Spiral')
axes[2].set_title('Fey Function')

plt.title('HW 01 Pranjal_Sept 14')

plt.xlabel('x')
plt.ylabel('y')
#problem: for some reason x and y are labelled just for the third plot and same if I create plt.title - it just adds it to the third one
plt.show() #and we get 2 plots on the same figure










































