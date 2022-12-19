import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math as m
import scipy.constants as const



mass = float(input('mass in kg? '))
R,theta,v_0,rho,C = .08,30*(m.pi)/180,100,1.22,.47            # in MKS system
g = 9.811

def dv_x(v_x,v_y):
    result = -((m.pi)*R**2*rho*C/(2*mass))*v_x*m.sqrt(v_x**2+v_y**2)
    return result


def dv_y(v_x,v_y):
    result = (-g-(((m.pi)*R**2*rho*C/(2*mass))*v_y*m.sqrt(v_x**2+v_y**2)))
    return result

v_0x = v_0*np.cos(theta)
v_0y = v_0*np.sin(theta)


t = [i/100 for i in range(1001)]
# print(t)
dt = t[1]-t[0]
x_vel = [v_0x]
y_vel = [v_0y]

x_pos = [0]
y_pos = [0]

for i in range(len(t)):
    vec = []
    v_x = dv_x(x_vel[i],y_vel[i])*dt
    v_y = dv_y(x_vel[i],y_vel[i])*dt
    x_vel.append(x_vel[i]+v_x)
    y_vel.append(y_vel[i]+v_y)
    x_pos.append(x_pos[i-1]+x_vel[i-1]*dt)
    y_pos.append(y_pos[i-1]+y_vel[i-1]*dt)
    
# print(x_vel[10], y_vel[10])
# # print(x_pos, y_pos)



# finding when the canonball hits the ground
abs_y = [abs(i) for i in y_pos]
cutt_off = abs_y.index(min(abs_y[10:1001]))


new_x = x_pos[0:cutt_off+1]
new_y = y_pos[0:cutt_off+1]
new_t = t[0:cutt_off+1]
x_range = new_x[cutt_off]



plt.plot(new_x,new_y)
plt.xlabel(r'x ', fontweight ='bold', fontsize = 15)
plt.ylabel('y', fontweight ='bold', fontsize = 15)

plt.title(f'Motion of the CanonBall. Calculated range = {x_range} meters')
plt.show()

print('Conclusion: increasing mass increases the range aymptotically to around 420 meters')









