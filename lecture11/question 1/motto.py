import os

file_name = "motto.txt"
try:
    path = os.path.dirname(os.path.abspath(__file__))
    f_handle = open(path+'/'+file_name,"r")
    f_handle.readline()
    f_handle.write("test")
except:
    print("failed")