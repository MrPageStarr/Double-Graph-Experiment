import seaborn as sns
from matplotlib import pyplot as plt

fig=plt.figure()
ax=fig.add_subplot()
data=[]
palette=sns.color_palette("seismic",10)

def init_animation(size):
  palette = list(reversed(sns.color_palette("seismic", size).as_hex()))
  ax.set_ylim(0, size)

def animation_function(i):
  
  frame = data[i]

  for idx in ax.containers:
    idx.remove()
    
  ax.bar(range(len(frame)),frame,color=palette)  