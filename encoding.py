
import math
import sys
from sys import argv
from struct import *

# Reading the input file from command line argument
input_string = open(sys.argv[1]).read() 

# Reading the bit_length from command line argument 
bit_length = int(sys.argv[2]) 

MAX_TABLE_SIZE = math.pow(2,bit_length)
print("The input_string is: ",input_string)

# Initializing the size of TABLE dictionary to 256 
size = 256 
# Initializing the empty TABLE dictionary to store all the characters with its ASCII values
TABLE = {} 
# Initializing the empty output_string_code list to store the encoded output values
output_string_code = [] 
# Initializing the initial_counter variable to 0 to store the index of the next input string
initial_counter = 0 
# Initializing the STRING variable as NULL
STRING = ""         

# function to define TABLE dictionary for each character with its ASCII value
def ASCII_dictionary(size):
    for i in range(size):
        TABLE[i] = chr(i)
    return TABLE

# function to get the length of input string
def get_len_of_input_string(input_string):
    return len(input_string)

# function to get the ASCII value from dicitionary
def get_key_from_dictionary(string,TABLE):
    key = [key for key, value in TABLE.items() if value == string][0]
    return key 

# function to write the output code data into the .lzw file in 16 bits binary format
def write_to_output_file(output_string_code,first_argv):
    output_file = open((first_argv).split(".txt")[0]+".lzw",'wb') 
    # for loop to convert each output_string_code in 16 bit format and write into the .lzw output file
    for itm in output_string_code:
        output_file.write(pack('>H',int(itm))) 
    output_file.close()

# function to encode the data and compress the input string
def enconding(initial_counter,STRING,TABLE,size):
    # define the TABLE dictionary by calling the ASCII_dictionary() function
    TABLE = ASCII_dictionary(size)
    # define the len_input_string by calling get_len_of_input_string() to iterarte over thge loop
    len_input_string = get_len_of_input_string(input_string) 
    # loop to check if there are still input SYMBOL characters in the input string
    while len_input_string >0:
        SYMBOL = input_string[initial_counter] 
    
        if (STRING + SYMBOL) in TABLE.values():
            STRING = STRING + SYMBOL
    
        else:
            # The key will hold the ASCII value of the new character which is added in the TABLE dictionary
            key = get_key_from_dictionary(STRING,TABLE)
            output_string_code.append(key) # The encoded data is appended to the output_string_code
            if len(TABLE) < MAX_TABLE_SIZE: # Check if the TABLE dictionary is not full
                   TABLE[size] = STRING + SYMBOL # The ASCII for new character will append at the end of the TABLE dictionary
    
            STRING = SYMBOL # Update the value of STRING with the SYMBOL
            # Increment the size variable so that the new character can be added with the new ASCII value in the TABLE dictionary
            size +=1     
        initial_counter +=1 # increment to fetch the next character from the input_string
        len_input_string -= 1 # len_input_string will reduce by 1 after each iteration
    
    # This Key will hold the ASCII value of the last character of the input_string
    key = get_key_from_dictionary(STRING,TABLE)
    output_string_code.append(key) #The last ASCII value will be appended to the output_string_code
    print(output_string_code) # Display the list of the output_string_code
    # Calling write_to_output_file() function to write the encoded data to the .lzw output file 
    write_to_output_file(output_string_code,sys.argv[1])

if __name__ == '__main__':
    if len(argv) == 3: # condition to check 3 arguments passed in command line: encoding.py input.txt Number_of_bits
        enconding(initial_counter,STRING,TABLE,size) # calling encoding function
    else:
        print("Invalid arguments passed, please check the arguments passed.\n")        

