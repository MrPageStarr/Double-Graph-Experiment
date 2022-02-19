import os
os.environ['MPLCONFIGDIR'] = '/tmp'
from random import shuffle
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