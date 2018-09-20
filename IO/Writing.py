#Author: Darpan Shah
#I/O Write Function for binary files
#Last Update: 20th September, 2018
import numpy as np
import io

#Write function
def WriteToBinary(row, col):
    #Creating a Binary file
    ran_ar = np.random.randint(0,5000000,10000)
    #Randomizing the input
    arr = []
    for x in ran_ar:
        x = bin(x)
        arr = np.append(arr,[x])

    print(arr)
    tmpfile = "tmpfile.bin"

    #Writing to the binary file
    file_ob = open("tmpfile.bin", mode='wb')
    print("\nwriting to file\n")
    val = arr.reshape(row,col)
    val.tofile(file_ob)
    print("\nwriting operation completed\n")
    file_ob.close()
