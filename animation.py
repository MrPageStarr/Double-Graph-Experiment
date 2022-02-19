import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

def function(i):
  global ax
  frame = data[i]
  
  for idx in ax.containers:
    idx.remove()
    
  ax.bar(range(len(frame)),frame,color=palette)

def init(size):
  global data,fig,ax,palette
  data=[]
  fig=plt.figure()
  ax=fig.add_subplot()
  palette = list(reversed(sns.color_palette("seismic", size).as_hex()))
  ax.set_ylim(0, size)

def show():
  animation = FuncAnimation(fig, function,
						frames=len(data),interval = 2)
  plt.show()

 