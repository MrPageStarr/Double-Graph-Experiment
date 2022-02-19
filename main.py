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
import animation as an
import sort as so

def create_random_list(length):
  some_list = [i for i in range(length)]
  shuffle(some_list)
  return some_list

sz= int(input("Enter number of elements to sort: "))

an.init(sz)
some_list=create_random_list(sz)
so.bubbleSort(some_list)
an.show()


