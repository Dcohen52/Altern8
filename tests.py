# test the following: lexer, parser, interpreter, builtins, errors, and the shell

# Path: lexer.py
from lexer import Lexer
from random import randint

INT = randint(0, 100)
SYMBOL = ['+', '-', '*', '/', '(', ')', '^', '%'][randint(0, 7)]
STRING = ['Z', 'Hello World', 'Random String', 'Another Random String', 'Yet Another Random String', 'A String'][randint(0, 5)]


def test_lexer():
    print('Testing lexer...\n')
    for t in [INT, SYMBOL, STRING]:
        lexer = Lexer('<stdin>', f'{t}')
        tokens = lexer.create_tokens()
        print(f'    {t} - {tokens}')


test_lexer()

# Path: parse.py
from parse import Parser

def test_parser():
    parser = Parser()


# Path: interpreter.py
def test_interpreter():
    pass


# Path: builtins.py

def test_builtins():
    pass


# Path: errors.py
def test_errors():
    pass


# Path: shell.py
def test_shell():
    pass
