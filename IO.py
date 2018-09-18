

#IO.py
#IO Data folder/directory creation module(in a temporary disk location)
#Project : LEEFS 
#Author: Darpan Shah
#Last update: 18th September, 2018

import os

#Creating a IO directory at a temporary disk location
def IO():
    IO_path = "/tmp/IO_Data_Directory"
    os.mkdir(IO_path, 755);
    print("IO_Data directory created in tmp folder.")

