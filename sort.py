import animation as an

def bubbleSort(some_list):
  an.data.append(some_list.copy())
  
  swapped = True

  while swapped:
    swapped = False
  
    for i in range(len(some_list)-1):
      if some_list[i] > some_list[i + 1]:
        some_list[i],some_list[i+1] = some_list[i+1],some_list[i]
        swapped = True
        an.data.append(some_list.copy())
        
  return some_list