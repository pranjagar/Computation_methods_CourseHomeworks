import numpy as n
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import math as m


""" 
h,w = 1,1
points = 71
delta_x = w/points  
delta_y = h/points
 """

h,w = 1,1                # height and width of the plane
points = 71              # number of slices each dimension is cut into
delta_x = w/points       # sizes of each interval on the two dimensions
delta_y = h/points



custom_variables = float(input('Default charge positions (type 0) or custom inputs (1) ? '))

if custom_variables ==1:
    print('Please input desired positions of charges as values in bw 0 and 1.')
    x1 = float(input('x-position of the first charge : ') )
    y1 = float(input('y-position of the first charge : ') )
    x2 = float(input('x-position of the second charge : ') )
    y2 = float(input('y-position of the second charge : ') )
else:
    x1,y1,x2,y2 = .45,.5,.55,.5
    print('Default charges set at x1,y1,x2,y2 = .45,.5,.55,.5.')

Log_or_linear_plot = float(input('Electric field plot in linear scale (type \'0\') or log scale (\'1\') ? '))


def r1(x,y):           #distance functions
    r =m.sqrt((x-x1)**2+(y-y1)**2)
    return r

def r2(x,y): 
    r =m.sqrt((x-x2)**2+(y-y2)**2)
    return r


def U(x,y):              # potential function
    U = 9e9*(1/(r1(x,y))+1/(r2(x,y)))
    return U


Potential_grid = n.zeros([points+1,points+1],float)   # starting with empty grid


for i in range(points+1):             # adding potential values  
    for j in range(points+1):
        x,y = i*delta_x, j*delta_y
        Potential_grid[points-j][i] = U(x,y,)



#making grids for plotting E field:
x= n.linspace(0,h,points+1)
y= n.linspace(0,w,points+1)
X,Y = n.meshgrid(x,y)

#finding partial derivatives
x_partial = n.zeros([len(Potential_grid),len(Potential_grid)], float)             # empty grids for partial derivatives
y_partial = n.zeros([len(Potential_grid),len(Potential_grid)], float)
k = 0                                                   # dummy variable for setting appropriate title in the plot


for i in range(1,len(Potential_grid)-1):        # adding partial derivative vaules to the empty grids above
    for j in range(1,len(Potential_grid)-1):
        x_partial[i,j] = ((Potential_grid[i+1,j]-Potential_grid[i-1,j])/(2*(delta_x)))
        y_partial[i,j] = ((Potential_grid[i,j+1]-Potential_grid[i,j-1])/(2*(delta_y)))


# For testing the quality of data, uncomment to use
""" 
test_array = n.zeros([len(x_partial),len(x_partial)], float)
small =0
large=0
for i in range(len(x_partial)):  #checking for too large elts in potential
    for j in range(len(x_partial)):
        if abs(x_partial[i,j]) > 1e12:
            # print(f'{[i,j]} is LARGE: ', x_partial[i,j]) 
            large+= 1
        elif abs(x_partial[i,j]) < 1:
            # print(f'{[i,j]} is SMALL: ', x_partial[i,j])
            small+= 1
            test_array[i,j] = x_partial[i,j]+10
print('Smalls : ', small, ' ,And larges : ', large)        
 """



if Log_or_linear_plot == 1:                               # the logarithm scaling
    for i in range(1,len(Potential_grid)-1):
        for j in range(1,len(Potential_grid)-1):
            if x_partial[i,j]> 1:
                x_partial[i,j] = n.log(abs(x_partial[i,j]))
            elif x_partial[i,j] < -1:
                x_partial[i,j] = -n.log(abs(x_partial[i,j]))
            if y_partial[i,j]> 1:
                y_partial[i,j] = n.log(abs(y_partial[i,j]))
            elif y_partial[i,j] < -1:
                y_partial[i,j] = -n.log(abs(y_partial[i,j]))
        k = 5 



fig,axes=plt.subplots(1,2,figsize=(13, 5))         # subplotting
axes[0].imshow(Potential_grid, extent=[0,w,0,h], norm = colors.LogNorm(vmin= 4e9, vmax= 5e12), cmap= 'inferno')
axes[1].quiver(X,Y, x_partial, y_partial)

axes[0].set_title('Electric Potential')
axes[0].set_xlabel("x")
axes[0].set_ylabel("y")

# fig.colorbar(axes[0])             # couldnt get the colorbar working

if k == 5:       # conditional for changing the title of the second graph
    axes[1].set_title('Electric field (log_e scale)')
else: 
    axes[1].set_title('Electric field (linear scale)')

axes[1].set_xlabel("x")
axes[1].set_ylabel("y")
 
plt.show()

