######################
###### IMPORTS #######
######################

from lexer import *
from parse import *
from interpreter import *
from context import *
from builtin import *
import sys
import tkinter as tk
import tkinter.filedialog
import os


######################
######   RUN   #######
######################

def run(fn, text):
    # Generate tokens
    lexer = Lexer(fn, text)
    tokens, error = lexer.create_tokens()
    if error: return None, error

    # Generate AST
    parser_ = Parser(tokens)
    ast = parser_.parse()
    if ast.error: return None, ast.error

    # Run Program
    interpreter = Interpreter()
    context = Context('<program>')
    context.symbol_table = global_symbol_table
    result = interpreter.visit(ast.node, context)
    return result.value, result.error


def close():
    sys.exit(0)


def documentation():
    docs_reserved = """
            -----------------------RESERVED------------------------
            - null: Return nothing.
            - true: Return true.
            - false: Return false.
            - math_pi: Return pi.
        """

    docs_general = """
            -------------------------GENERAL------------------------
            For now, Altern8 support only double-quotes ("), we currently working on support for (') single-quotes as well.
            
            - run(): Run ".alt8" files: "run -f" for choosing *.alt8 file using file dialog, "run -t" to run a test file from your desktop, or "run("examples/example.alt8")" for running *.alt8 using a specific path.
            - clear(): Clean the screen - Linux/macOS systems.
            - cls(): Clear the screen - Windows systems.
            - null(): Return nothing.
            - quit(): Quit the interpreter CLI.
        """

    docs_print_var = """
            -----------------------PRINT & VAR----------------------
            - print(): Print something to the console.
            - Variable declaration: var x = 5 -> will print "5" to the console.
        """

    docs_checking = """
            ------------------------CHECKING------------------------
            - is_num(): Returns boolean value whether the input is a num or not (0/1).
            - is_str(): Returns boolean value whether the input is a string or not (0/1).
            - is_list(): Returns boolean value whether the input is a list or not (0/1).
            - is_func(): Returns boolean value whether the input is a function or not (0/1).
        """

    docs_lists = """
            -------------------------LISTS--------------------------
            - append(): Appends to list.
            - len(): Return the length of the variable.
            - pop(): Remove item from a list.
            - extend(): Combine two lists.
        """

    docs_read = """
            -------------------------READ---------------------------
            - read(): Read string input from the user.
            - read_int(): Read numerical input from the user.
        """

    docs_additional = """
            -----------------------FUNCTIONS------------------------
            - get_functions(): Get all the functions from a file.
        """

    docs = docs_general + docs_print_var + docs_checking + docs_lists + docs_read

    print("""Welcome to Altern8's docs!

Altern8 is a unique blend of different programming paradigms. 
It has the familiarity of JavaScript in terms of reserved words and the structured coding flow of C++. 
Altern8 is kind of a mix of JavaScript, Python, C++ & Kotlin. 

Available commands: general, print_var, checking, lists, read, additional, full, quit""")

    def read_line_gen(s):
        for line in s.split('\n'):
            yield line.strip()

    while True:
        command = input("docs > ")
        match command:
            case 'general':
                for line in read_line_gen(docs_general):
                    print(line)
            case 'print_var':
                for line in read_line_gen(docs_print_var):
                    print(line)
            case 'checking':
                for line in read_line_gen(docs_checking):
                    print(line)
            case 'lists':
                for line in read_line_gen(docs_lists):
                    print(line)
            case 'read':
                for line in read_line_gen(docs_read):
                    print(line)
            case 'additional':
                for line in read_line_gen(docs_additional):
                    print(line)
            case 'full':
                for line in read_line_gen(docs):
                    print(line)
            case 'quit':
                break
            case _:
                print(
                    "Invalid command. Available commands: general, print_var, checking, lists, read, additional, full, quit")
