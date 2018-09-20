#Author: Darpan Shah
#I/O Read Function for binary files
#Last Update: 20th September, 2018
import numpy as np
import io



#Read function for binary files
def ReadFromBinary(row,col):
    f = open("tmpfile.bin", "rb")
    print("\nreading file\n")
    
    #Reading for all rows: setting up the counter
    counter = row
    m = []

    while counter >0:
        r = np.fromfile(f, dtype = np.uint8, count=col,sep="")
        m = np.append(m,r)
        counter = counter - 1


    m.reshape(row,col)
    print(m)
    print("\nreading operation completed\n")
