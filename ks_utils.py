# Routine used in my_tests.py to read input-data from a string!
import sys
def from_data_to_words(input_data):
    f = open(input_data, 'r')
    try:
        words = f.read().split('\n')
        first_word = words[0]
        second_word = words[1]

    except:
        print("No existe el fichero")
        sys.exit()

    return first_word, second_word

    

