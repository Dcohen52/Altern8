![alt8 long](https://user-images.githubusercontent.com/26333525/232536382-482f6a8e-66ab-40f0-a7f0-c5374aea14d3.png)


# Altern8
Altern8 is a programming language implemented using Python, this language has been built for educational purposes only and not intended for building large-scale applications yet. This repository includes a lexer, parser, and interpreter. Altern8 has been inspired by prominent languages such as JavaScript, Python, C++, and Kotlin. Example programs can be found in the examples folder.

## Setup and Usage
* Clone this repository.
* Run shell.py in the command line: `python shell.py`
* The Altern8 interpreter will open. To execute an Altern8 program, pass the path of the Altern8 file to the `run()` function: `run("modules\example_2.alt8")`

# Language Features
## Data Types
Altern8 supports the following data types:

* **Variables:** Variables can be declared using the var keyword and can be reassigned using the $ symbol.
* **Lists:** Altern8 supports basic list operations, including adding and removing elements, extending lists, and accessing elements by index.
* **Strings:** Strings can be concatenated, embedded with variable values, and checked for being a string using the is_str() function.

## Operators
Altern8 supports the following operations:

* **Arithmetic:** `+, -, *, /, %, ** (power)`
* **Relational:** `<, >, <=, >=, !=, ==`
* **Logical:** `and, or, not`
* **Bitwise:** `&, |, ^, ~`

## Input and Output
* **User input:** Use the `input()` function to get input from the user. For integer input, use the `input_int()` function.
* **Print:** The `print` function is used to display output on the console screen. It has two parameters: `output` and `separator`.

## Control Flow
Altern8 supports the following control flow structures:

* **For loops:** Loop over a block of statements a specified number of times.
* **While loops:** Loop over a block of statements while a condition is true.
* **If statements:** Execute a block of code if a condition is true. Altern8 also supports elif for checking multiple conditions and else for executing code when all conditions are false.

## Functions
Altern8 supports both named and anonymous functions. Functions can be declared using the define keyword and can be assigned to variables. The `is_func()` function can be used to check if an element is a function.

---

# The Altern8 Shell: A Command-Line Interface for the Altern8 Language

The Altern8 Shell is a sophisticated command-line interface designed for interacting with the Altern8 programming language. The shell supports a range of essential operations such as executing Altern8 scripts, processing user inputs, and displaying output. Additionally, it offers an array of built-in commands to manage and manipulate scripts efficiently.

## Initiating the Altern8 Shell
To launch the Altern8 Shell, execute the `shell.py` script via the terminal:

`python shell.py`

## Loading and Running Altern8 Files
The shell offers several ways to load and run Altern8 files:

1. Use the `run()` command followed by the path to the Altern8 file:
`run("path/to/your/script.alt8")`
2. Use the `run -f` command to open a file dialog and choose an Altern8 file:
`>>> run -f`
3. Use the `run -t` command to load and run a test file from your desktop:
`>>> run -t`


## Built-in Commands
The shell provides several built-in commands for working with Altern8 scripts and managing the shell environment. Here is a summary of the available commands:

* **run():** Run an Altern8 file. *See the section above for different ways to load and run files.*
* **quit:** Quit the interpreter CLI.
* **docs:** Access the Altern8 documentation.

For more information on these commands and additional functionality, type docs in the shell to access the Altern8 documentation.

## Language Examples
Please refer to the original README file for examples of each language feature in Altern8 syntax.

## Changelog

0.0.1 - Initial Release
First release of Altern8.
Basic language functionality implemented.
0.0.2 - New Builtin Function Added
Added a new builtin function get_functions() to retrieve functions from an .alt8 file.
