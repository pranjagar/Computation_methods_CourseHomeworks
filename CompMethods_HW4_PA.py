import numpy as n
import random as r
import matplotlib.pyplot as plt
import scipy.constants as const
import math as m



# defining constants
G = const.gravitational_constant
M = 5.97219*1e24
m =  7.348e22
R = 3.844e8
w = 2.662e-6

# defining the function as f(x) = 0
def f(r): return (G*M/(r**2)-G*m/((R-r)**2)-w**2*r)

# defining the analytic derivative expression
def deriv(r) : return (-2*G*M/(r**3)-2*G*m/((R-r)**3))- w**2

# defining the numerical derivative function
def df(x):
    h = .0001
    y = (f(x+h)-f(x))/h
    return y 

r = 1000              # starting initial value
y =1                  # (dummy) starting output value

while y > 1e-3:                          # newton's method loop
    r -= f(r)/(deriv(r))                # r is modified according the newton/secant method
    y = f(r)                              # dummy value is reassigned as the output number
print(f'\nNewton Raphson method solution is {r} meters \n')
# checking if the solution worked
print(f'Plugging in Newton method solution gives: {f(r)}')
if f(r) < 1e-3:
    print('The solution works! \n')


while y > 1e-3:                         # secant method loop
    r -= f(r)/(df(r))
    y = f(r) 
print(f'Secant method solution is {r} meters \n')
# checking if the solution worked
print(f'Plugging in Secant method solution gives: {f(r)}')

if f(r) < 1e-3:
    print('The solution works! \n')
