# 8-12-2022
# most-chars.py 
# A program that takes a text filename as command-line argument and
# prints the word containing the largest number of a chosen letter


import sys


def validity_check(file_length):
    '''stops program & sends error message if conditions are not right'''
    if file_length > 20:
        sys.stderr.write("Input file is too large. Use a file with no more than 20 lines\n")
        exit(-1)
    elif file_length == 0:
        sys.stderr.write("Input file is empty or contains no valid text\n")
        exit(-1)
    elif len(sys.argv) != 3:
        sys.stderr.write("Usage: requires 3 arguments, python3 <example.py> <example.txt> <char>\n")
        exit(-1)
    elif len(sys.argv[2]) != 1:
        sys.stderr.write("Please enter a single character\nUsage: python3 <example.py> <example.txt> <char>\n")
        exit(-1)
    elif not sys.argv[0].endswith(".py") or not sys.argv[1].endswith(".txt"):
        sys.stderr.write("Incompatible file extension(s). Please use .py and .txt files respectively\n")
        exit(-1)


def compare_char_amount(char, word1, word2):
    '''returns the word containing less of the chosen character'''
    if word1.lower().count(char) < word2.lower().count(char):
        return word1
    else:
        return word2


def find_most_chars(word_list, char):
    '''recursively finds word in a list containing  most of a character'''
    if len(word_list) > 1:
        word_list.remove(compare_char_amount(char, word_list[0], word_list[1]))
        return find_most_chars(word_list, char)
    return word_list[0]


def main():
    infile_test = open(sys.argv[1], "r")
    file_length = len(infile_test.readlines())
    infile_test.close()

    infile = open(sys.argv[1], "r")
    word_list = infile.read().split()
    infile.close()

    validity_check(file_length)
    chosen_char = str(sys.argv[2]).lower()
    most_char_word = find_most_chars(word_list, chosen_char)
    if chosen_char not in most_char_word:
        sys.stderr.write("This file does not contain the character " + chosen_char + '\n')
        exit(-1)
    else:
        sys.stdout.write("result: " + most_char_word  + '\n')


if __name__ == '__main__':
    main()
