# LZW-Compression-and-Decompression


Project: LZW Compression and Decompression


- Program Design:

Data Structures Used in encoding.py and decoding.py programs: 
Dictionary - Dictionary with keys as ASCII values, values as string
List - to store the encoded ASCII values

Time Complexity: 
The time complexity to search and appending in the TABLE dictionary is O(1). 
And the time complexity for appending and reading from the ASCII code in the list is O(1).

- Brief summary of the encoding.py program:

1. The encoding.py will receive two command-line arguments from the user:
    i. <input_file.txt>: The path to an input file in .txt format containing the data to be encoded.
    ii. <bit_length>: An integer representing the bit length used for encoding.
2. Next, the data is read from the specified input file.
3. The maximum dictionary size is calculated using Math.pow(2, bit_length). This determines the maximum number of entries that the dictionary can hold based on the specified bit length.
4. After that, a dictionary is initialized to store and retrieve characters. It starts with an initial set of 256 ASCII characters, this dictionary serves as the basis for the encoding process.
5. The input data is processed character by character, appending to the TABLE dictionary as new codes come up. It generates encoded sequences for the data, storing them compactly as 2-byte representations. The resulting encoded sequences are saved in the input.lzw file.

- Brief summary of the decoding.py program:

1. The decoding.py receives two command-line arguments from the user:
    i. <encoded_input_file.lzw>: The path to the input file in LZW format obtained from encoding.
    ii. <bit_length>: An integer representing the bit length used during encoding.
2. The data is read from the specified input.lzw file. 
3. The maximum dictionary size is calculated using Math.pow(2, bit_length). This determines the maximum number of entries that the dictionary can hold based on the specified bit length.
4. After that, a dictionary is initialized to handle decoding. It starts with an initial set of 256 ASCII values as keys and their respective characters as values. 
5. The encoded data is decoded by reconstructing numerical sequences, dynamically building a dictionary for new codes, and generating a decoded string using this dictionary. The resulting decoded data is stored in a '<input>_decoded.txt' file.

- Breakdown of the files:

encoding.py:    
Encoder file encodes the string from 'input.txt' file as
Input: The Encoder file takes the command line input as <input_file.txt> and bit_length 
Output: The Encoder file generates the output file as <input_file.lzw>

decoding.py:    
Decoder file which decodes the encoded input data as
Input: The Decoder file takes the command line input as <input_file.lzw> and bit_length     
Output: The Decoder file generates the output file as '_decoded.txt' format 


- what works and what fails:

Both the ecoding and decoding files works for all cases of input string file. It will throw error if the user passes invalid input arguments in the command line.
The following message will appear in the terminal:
"Invalid arguments passed, please check the arguments passed"

- programming language and compiler version

Programming Language Used: Python 
Compiler Version: 3.12.0

- Steps to run the Project:

1. Place encoding.py and decoding.py within a single folder.
2. Create a text file named input.txt in the same folder and write the input string in this text file.
3. Prompt the user to enter the input file name and the desired bit length as command line arguments.
4. Begin by executing the encoding.py file:
        Syntax: python encoding.py <input_file.txt> <bit_length>
        Example: python encoding.py input.txt 16
5. This will generate an .lzw file which will contain the encoding data and it will be stored in the same folder as the other files. 
6. Next, execute the decoding.py file:
        Syntax: python decoding.py <encoded_input_file.lzw> <bit_length>
        Example: python decoding.py input.lzw 16
7. This will generate a text file which will be the decoded output file in the '<input file name>_decoded.txt' format which will be stored in the same folder.
8. To execute multiple files, follow the same Steps with different input files as arguments in the command line.


