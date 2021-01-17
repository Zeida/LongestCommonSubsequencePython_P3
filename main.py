import argparse
import datetime
import pathlib
from ks_utils import *
from prueba import *
from solve_memoization import *
from solve_tabulation import *

# mejorar con argparse

if __name__ == '__main__':

    my_parser = argparse.ArgumentParser(
        description='Longest Common Subsequence Problem (Not required to occupy consecutive positions)')

    my_parser.add_argument('-hf',
                           action='store_true',
                           help='Show how should the file be structured')

    my_parser.add_argument('-sm',
                           action='store_true',
                           help='Solve it with Memoization')

    my_parser.add_argument('-st',
                           action='store_true',
                           help='Solve it with Tabulation')

    my_parser.add_argument('-f',
                           '--file',
                           type=str,
                           action='store',
                           nargs=1,
                           help='File (process a single file)')

    my_parser.add_argument('-d',
                           '--directory',
                           type=str,
                           action='store',
                           nargs=1,
                           help='Directory (process many files)')

    my_parser.add_argument('-check',
                           action='store_true',
                           help='Check Solutions_[Must be used with -sm and -st]')

    my_parser.add_argument('-show',
                           action='store_true',
                           help='Show the content of the file')

    my_parser.add_argument('-t',
                           action='store_true',
                           help='Display time')

    my_parser.add_argument('-input',
                           action='store_true',
                           help='Allow to introduce the words on the console')

    my_parser.add_argument('-lcs',
                           action='store_true',
                           help='Show the longest common subsequence')

    my_parser.add_argument('-p',
                           action='store_true',
                           help='Pruebas de código')

    args = my_parser.parse_args()

    # leemos el fichero pasado como parámetro si existe
    if args.file:
        first_word, second_word = from_data_to_words(args.file[0])

        if args.show:
            print("First word is: " + first_word)
            print("And second word is: " + second_word)
            print("")

        if args.sm:
            print("###########################_Memoization_##############################")
            inicio = datetime.datetime.now().timestamp()
            c = FILL_LCS(first_word, second_word)
            smlength = LCSLength(first_word, second_word, c, 0, 0)
            print("The longest common subsequence has size: " + str(smlength))
            fin = datetime.datetime.now().timestamp()
            print("")

            if args.t:
                tiempo = fin - inicio
                print("Time consumed by Memoization: " + str(round(tiempo, 3)) + " seg ")
                print("")
            if args.lcs:
                print('Longest Common Subsequence: ', end='')
                SMLCS(first_word, second_word, c)


        if args.st:
            print("###########################_Tabulation_##############################")
            inicio = datetime.datetime.now().timestamp()
            stlength, solst = LCS(first_word,second_word)
            print("The longest common subsequence has size: " + str(stlength))
            fin = datetime.datetime.now().timestamp()
            print("")

            if args.t:
                tiempo = fin - inicio
                print("Time consumed by Tabulation: " + str(round(tiempo, 3)) + " seg ")
                print("")

            if args.lcs:
                print("LCS is " + "".join(solst))
                print("")

        if args.check:
            if stlength == smlength:
                print("Tabulation and Memoization has the same solution. ")
                print("")
            else:
                print("Solutions dont match. There must be a mistake.")
                print("")



    if args.directory:
        dir = args.directory[0]
        directorio = pathlib.Path(dir)

        for fichero in directorio.iterdir():
            first_word, second_word = from_data_to_words(fichero)

            if args.show:
                print("First word is: " + first_word)
                print("And second word is: " + second_word)
                print("")

            if args.sm:
                print("###########################_Memoization_##############################")
                inicio = datetime.datetime.now().timestamp()
                c = FILL_LCS(first_word, second_word)
                smlength = LCSLength(first_word, second_word, c, 0, 0)
                print("The longest common subsequence of "+ str(fichero.name)+" has size: " + str(smlength))
                fin = datetime.datetime.now().timestamp()
                print("")
                if args.t:
                    tiempo = fin - inicio
                    print("Time consumed by memoization: " + str(round(tiempo, 3)) + " seg ")
                    print("")
                if args.lcs:
                    print('Longest Common Subsequence of: ', str(fichero.name), "is: ", end='')
                    SMLCS(first_word, second_word, c)

            if args.st:
                print("###########################_Tabulation_##############################")
                inicio = datetime.datetime.now().timestamp()
                stlength, solst = LCS(first_word,second_word)
                print("The longest common subsequence of " + str(fichero.name)+" has size: " + str(stlength))
                fin = datetime.datetime.now().timestamp()
                print("")

                if args.t:
                    tiempo = fin - inicio
                    print("Time consumed by Tabulation: " + str(round(tiempo, 3)) + " seg ")
                    print("")

                if args.check:
                    if stlength == smlength:
                        print("Tabulation and Memoization has the same solution. ")
                        print("")
                    else:
                        print("Solutions dont match. There must be a mistake.")
                        print("")

                if args.lcs:
                    print("LCS is " + "".join(solst))
                    print("")

    if args.input:

        print("Introduce the first word: ")
        first_word = input()

        print("Introduce the second word: ")
        second_word = input()

        print("")

        if args.show:
            print("First word is: " + first_word)
            print("And second word is: " + second_word)
            print("")

        if args.sm:
            print("###########################_Memoization_##############################")
            inicio = datetime.datetime.now().timestamp()
            c = FILL_LCS(first_word, second_word)
            smlength = LCSLength(first_word, second_word, c, 0, 0)
            print("The longest common subsequence has size: " + str(smlength))
            fin = datetime.datetime.now().timestamp()
            print("")

            if args.t:
                tiempo = fin - inicio
                print("Time consumed by Memoization: " + str(round(tiempo, 3)) + " seg ")
                print("")

            if args.lcs:
                print('Longest Common Subsequence: ', end='')
                SMLCS(first_word, second_word, c)

        if args.st:
            print("###########################_Tabulation_##############################")
            inicio = datetime.datetime.now().timestamp()
            stlength, solst = LCS(first_word,second_word)
            print("The longest common subsequence has size: " + str(stlength))
            fin = datetime.datetime.now().timestamp()
            print("")

            if args.lcs:
                print("LCS is " + "".join(solst))
                print("")

            if args.t:
                tiempo = fin - inicio
                print("Time consumed by Tabulation: " + str(round(tiempo, 3)) + " seg ")
                print("")

        if args.check:
            if stlength == smlength:
                print("Tabulation and Memoization has the same solution. ")
                print("")
            else:
                print("Solutions dont match. There must be a mistake.")
                print("")




    if args.hf:
        print("")
        print("Text file structure should be:")
        print("")
        print("1. The first line is the first word")
        print("")
        print("2. The second line is the second word")
        print("")

    if args.p:
        print("### PRUEBAS ###")
        c = FILL_LCS(first_word, second_word)
        len=LCSLength(first_word, second_word, c, 0, 0)
        print(len)
        print('Longest Common Subsequence: ', end='')
        SMLCS(first_word, second_word, c)

