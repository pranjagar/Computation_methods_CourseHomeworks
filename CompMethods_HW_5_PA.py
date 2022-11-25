import numpy as n
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import scipy.fftpack as fft
import argparse


# Creating ArgParse thing
parser = argparse.ArgumentParser(description= 'enter following arguments: data_period, type of fourier transform, percent')
parser.add_argument("data_period", type= str, help= "enter which data : 'dow' or 'dow2' " )
parser.add_argument("type_of_ft", type= str, help= "enter which type of fourier transform : 'ft' or 'fct' " )
parser.add_argument("percent", type= float, help= "enter percent value for reconstructing from fourier coefficients")
args = parser.parse_args()

textfile = str(args.data_period)+'.txt'            # textfile variable to select between dow.txt and dow2.txt
percentvalue = args.percent                         # variable to change the percent of fourier transfomred data from the beginning to keep and remaining to make zero

y = n.loadtxt(textfile, dtype= float)                # y and x are the list containg data and numbers enumerating that, respectively
x = list(range(1,len(y)+1))


ft = fft.fft(y)                                     # fourier transforining the data
fct = fft.dct(y)                                    # fourier cosine transforining the data

type_of_ft = str(args.type_of_ft)                       # assingng variable for choosing in between fourier and fourier cosine transform
if type_of_ft == 'ft':
    transform = ft
    title_word = 'fourier transform'
elif type_of_ft == 'fct':
    transform = fct
    title_word = 'fourier cosine transform'


# keeping given percent of points form the begninning 
percentlength = percentvalue*len(ft)//100
tenpercentlistFT = [transform[i] if i<(percentlength+1) else 0 for i in range(len(transform))]


if type_of_ft == 'ft':                                      # creating inverse transforms. 'idct' function gives worse results
    inverseTransform = fft.ifft(tenpercentlistFT)
elif type_of_ft == 'fct':
    inverseTransform = fft.idct(tenpercentlistFT)

plt.plot(x,y)                                                       # the original data curve, marked iin blue
plt.plot(list(range(len(inverseTransform))), inverseTransform)          # the recreated data curve using inverses transform, color yellow
plt.title(f'Dow data vs reconstruction using first {int(percentvalue)} percent values of it\'s {title_word}')   # title
plt.show() 









