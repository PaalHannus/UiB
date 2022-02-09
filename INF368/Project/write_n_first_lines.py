
# Python program that reads a file and writes its first n lines to a new file with utf-8 encoding.

import sys
import os
import re
import codecs

# Function that reads a file and writes its first n lines to a new file with utf-8 encoding.


def write_n_first_lines(file_name, n):
    try:
        with codecs.open(file_name, 'r', encoding='utf-8') as file_object:
            lines = file_object.readlines()
            lines = lines[:n]
            with codecs.open(file_name + '_out.txt', 'w', encoding='utf-8') as out_file_object:
                for line in lines:
                    out_file_object.write(line)
    except IOError as error:
        print('File error: ' + str(error))


def main():
    print(len(sys.argv))
    if len(sys.argv) == 3:
        file_name = sys.argv[1]
        n = int(sys.argv[2])
        write_n_first_lines(file_name, n)
    else:
        print('Usage: ' + sys.argv[0] + ' <file_name> <n>')


main()
