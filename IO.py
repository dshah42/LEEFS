

#IO.py
#IO Data folder/directory creation(in a temporary disk location)
#Project : LEEFS 
#Author: Darpan Shah
#Last update: 18th September, 2018

import os

#Creating a IO directory at a temporary disk location
def IO():
    IO_path = "/tmp/IO_Data_Directory"
    os.mkdir(IO_path, 755);
    print("IO_Data directory created in tmp folder.")

def main():
    IO();
    
main()

#Removal for cleanup, when necessary
os.rmdir("/tmp/IO_Data_Directory")
print("IO Data directory removed from tmp folder.")
