import numpy as np

arr = np.array([[i for i in range(6)], [i for i in range(10,16)],[i for i in range(20,26)],[i for i in range(30,36)],[i for i in range(40,46)],[i for i in range(50,56)]])

# Use slice methods to print out the highlighted boxes
a0 = arr[:,1] # blue box | figure out how to get rid of np.int
a1 = arr[1,2:4] # pink box | figure out how to get rid of the array name
a2 = arr[2:4,4:] # green box
a3 = [arr[2, 0::2].tolist(), arr[4, 0::2].tolist()] # orange | get rid of
print(arr)
print(a0)
print(a1)
print(a2)
print(a3)