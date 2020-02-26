import csv
import sys
import os

######################################################################################
# Author: Branden Walter                                                             #
# Description: Takes in a csv file and prints the email column to a new text file    #
######################################################################################

def main():
    
    #full path of the input file and output file
    filename_in = 'emails.csv'
    filename_out = 'email_list.txt'
    filename_dir_in = os.path.dirname(os.path.abspath(__file__)) + '\\' + filename_in
    filename_dir_out = os.path.dirname(os.path.abspath(__file__)) + '\\' + filename_out
    
    #opens the given input and output files
    file_in = open(filename_dir_in, 'r', encoding="utf8")
    file_out = open(filename_dir_out, 'w', encoding="utf-8")
    
    #converts file_in and uses the csv module
    reader = csv.reader(file_in)

    #Finds header of file
    header = next(reader, None)

    #Index of the Email column
    index = header.index('Email')

    #loop through every line in csv file
    for line in reader:
        #skips the empty cells
        if line[index] == '':
            pass
        else:
            #Writes emails and a new line char to the new text file
            finished = str(line[index]) + '\n'
            file_out.write(finished)
            
    #Closes the file streams
    file_in.close()
    file_out.close()


if __name__ == "__main__":
    main()