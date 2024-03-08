'''
Name: Himanshu Kiran Garud
Student ID: 801365910
University Mail: hgarud@uncc.edu
Course: ITCS-6114
'''

import math
import sys
from sys import argv
from struct import *

# Reading the input file from command line argument
input_string_file = open(sys.argv[1],"rb").read() 
# Reading the bit_length from command line argument 
bit_length = int(sys.argv[2]) 

# Initializing the size of TABLE dictionary to 256 
size = 256 
# Initializing the empty TABLE dictionary to store all the characters with its ASCII values
TABLE = {} 
# Initializing the empty input_code list to store all the encoded ASCII values
input_code = [] 
# Defining the MAX_TABLE 
MAX_TABLE = math.pow(2,bit_length)

# function to unpack the encoded input_string_file and return it as a list
def unpack_string(input_string_file):
    # The length of the file divide by 2 as unsigned short integer takes 2 bytes in the binary data
    st_int = len(input_string_file) // 2 
    frm_str = '>'+'H' * (st_int)
    inp_str = unpack(frm_str, input_string_file)
    return list(inp_str)

# function to define TABLE dictionary for each character with its ASCII value
def ASCII_dictionary(size):
    # loop to assign ASCII value to each character in the TABLE dictionary
    for i in range(size):
        TABLE[i] = chr(i)
    return TABLE

# function to write the output string data into the _decoded.txt file
def write_to_output_file(output_string,first_argv):
    output_file = open((first_argv).split(".lzw")[0]+"_decoded.txt",'w')
    # Converted each output_string_code and write into the _decoded.txt output file  
    output_file.write(output_string) 
    output_file.close()

# function to decode the encoded code into string    
def decoding(input_string_file,size,TABLE):
    # input_code() function to store ASCII code
    input_code = unpack_string(input_string_file)
    print("The encoded code is: \n",input_code)
    TABLE = ASCII_dictionary(size)
    # Variable to store the input_code, initially it will store the first input code
    CODE = input_code[0] 
    # Variable to store the character for the code
    STRING = TABLE[CODE]
    # Variable to store the new character that is not defined in the TABLE dictionary
    NEW_STRING = ""
    # Variable to iterate over the loop
    initial_counter = 1
    len_of_input_string = len(input_code)
    # Variable to store the decoded string
    output_string = ""
    output_string += STRING
    # loop to check if there are still input codes to be decoded
    while len_of_input_string >= 1 and initial_counter < len(input_code):
        # Reading next code from encoded list
        CODE = input_code[initial_counter]  
        initial_counter +=1
        # Condition to check if the encoded code is present in the TABLE dicitionary or not
        if CODE not in TABLE:
            NEW_STRING = STRING + STRING[0]
        else:
            NEW_STRING = TABLE[CODE]
        # Updating the output_string variable with the NEW_STRING variable data   
        output_string += NEW_STRING
        # Condition to check if the TABLE is full or not
        if len(TABLE) < MAX_TABLE:
            TABLE[size] = STRING + NEW_STRING[0]
            size +=1
        STRING = NEW_STRING
        len_of_input_string -=1
    # Calling write_to_output_file() to write the decoded output to the _decoded.txt file   
    write_to_output_file(output_string,sys.argv[1])
    print(output_string)

if __name__ == '__main__':
    if len(argv) == 3: # condition to check 3 arguments passed in command line: decoding.py input.lzw Number_of_bits
        decoding(input_string_file,size,TABLE) #Calling the decoding function
    else:
        print("Invalid arguments passed, please check the arguments passed.\n")        
    

