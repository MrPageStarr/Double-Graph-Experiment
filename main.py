# make sure the library os is imported
import os

#then set the 'MPLCONFIGDIR' to '/tmp'
os.environ['MPLCONFIGDIR'] = '/tmp'
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html
import matplotlib.pyplot as plt
import numpy as np        # numeric python
from random import shuffle
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation, writers
import numpy as np

def create_random_list(length):
  some_list = [i for i in range(length)]
  shuffle(some_list)
  return some_list

def animation_function(i):
  
  frame = animList[i]
  
  for idx in ax.containers:
    idx.remove()
    
  ax.bar(range(len(frame)),frame,color=palette)

sz= int(input("Enter number of elements to sort: "))
palette = list(reversed(sns.color_palette("seismic", sz).as_hex()))
fig=plt.figure()
ax=fig.add_subplot()
ax.set_ylim(0, sz)

some_list=create_random_list(sz)
animList=[some_list]

swapped = True

while swapped:
  swapped = False
  for i in range(len(some_list)-1):
    if some_list[i] > some_list[i + 1]:
      some_list[i],some_list[i+1] = some_list[i+1],some_list[i]
      swapped = True
      animList.append(some_list.copy())

	


animation = FuncAnimation(fig, animation_function,
						frames=len(animList),interval = 2)
plt.show()

