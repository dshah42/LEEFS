

#IO.py
#IO Data folder/directory creation module(in a temporary disk location)
#Project : LEEFS
#Author: Darpan Shah
#Last update: 20th September, 2018

import numpy as np
import io
import os

#Creating a IO directory at a temporary disk location
def IO():
    IO_path = "/tmp/IO_Data_Directory"
    os.mkdir(IO_path, 755);
    print("IO_Data directory created in tmp folder.")

#Write function for binary files
def write_func(row, col):
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


#Read function for binary files
def read_func(row,col):
    f = open("tmpfile.bin", "rb")
    print("\nreading file\n")

    #Reading for all rows: setting up the counter
    counter = row
    m = []

    while counter > 0:
        r = np.fromfile(f, dtype = np.uint8, count=col,sep="")
        m = np.append(m,r)
        counter = counter - 1


    m.reshape(row,col)
    print(m)
    print("\nreading operation completed\n")
