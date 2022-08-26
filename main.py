# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy
import numpy as np
from sympy import *
from sympy.parsing.sympy_parser import parse_expr


def main():
    # Use a breakpoint in the code line below to debug your script.
    print("Welcome to a Math solver.")
    print("Just enter name of a concept and what you want to compute. I will do the rest!")
    while True:
        input_text = str(input("Enter concept and then problem (press q to quit): "))

        if input_text == 'q':
            print("Bye-bye")
            break

        if input_text[0:10].lower() == 'derivative':
            result_string = input_text[11:]
            x_symbol = {'x': Symbol('x', real=True)}
            function = parse_expr(result_string, x_symbol)
            differential = diff(function, x_symbol['x'])
            print(differential)

        if input_text[0:8].lower() == 'integral':
            result_string = input_text[9:]
            x_symbol = {'x': Symbol('x', real=True)}
            function = parse_expr(result_string, x_symbol)
            integral = integrate(function, x_symbol['x'])
            print(integral)

        if input_text[0:11].lower() == 'rref matrix':
            rows = int(input("Enter number of rows of the matrix: "))
            cols = int(input("Enter number of columns of the matrix: "))
            matrix = []
            for i in range(rows):
                list_row = str(input("Enter numbers of a row separated by space: "))
                list_row_to_append = []
                for j in range(cols):
                    list_row_to_append.append(list_row[2*j])
                matrix.append(list_row_to_append)
            good_matrix = Matrix(matrix)
            rref = good_matrix.rref()
            print("The RREF is: " + rref[0])

        if input_text[0:29].lower() == 'solve system linear equations':
            rows_a = int(input("Enter number of rows of the matrix A: "))
            cols_b = int(input("Enter number of columns of the matrix A: "))
            matrix_a = []
            for i in range(rows_a):
                list_row_a = str(input("Enter numbers of a row (matrix A) separated by space: "))
                list_row_a_to_append = []
                for j in range(cols_b):
                    list_row_a_to_append.append(list_row_a[2*j])
                matrix_a.append(list_row_a_to_append)
            a = numpy.array(list(matrix_a))

            rows_b = int(input("Enter number of rows of the matrix B: "))
            cols_b = int(input("Enter number of columns of the matrix B: "))
            matrix_b = []
            for i in range(rows_b):
                list_row_b = str(input("Enter numbers of a row (matrix B) separated by space: "))
                list_row_b_to_append = []
                for j in range(cols_b):
                    list_row_b_to_append.append(list_row_b[2 * j])
                matrix_b.append(list_row_b_to_append)
            b = numpy.array(list(matrix_b)) 

            x = numpy.linalg.solve(a, b)

            print("The result is: " + x)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
