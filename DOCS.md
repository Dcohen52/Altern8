# Altern8 Documentation
Altern8 is a programming language that has a lexer, parser, and interpreter written in Python. It provides basic functionalities like arithmetic, relational, logical, and bitwise operations. The language supports variables, user input, printing to console, lists, strings, for loop, while loop, if statements, and functions.

### Running Altern8 Programs
To run Altern8 programs, first download the repository. Then, run the shell.py file in the command prompt using the following command: `python shell.py`. This will open the Altern8 interpreter. Pass the path of the Altern8 program to the run() function to execute Altern8 programs. For example, to run the factorial program located in the examples folder, use run("examples\factorial.alt8").

---

### Variables
Variables in Altern8 can be assigned using the var keyword. For example: `var a = 5`. The values of variables can be reassigned using the `$` symbol. For example: `$a = 6`.

### User Input
User input in Altern8 can be obtained using the `input()` function. For integer input, the `input_int()` function can be used.

## Printing
The `print()` function is used to print output to the console screen. It has two parameters: `output` and `separator`. For example:
```
print("Hello", " ")
print("World", " ")
```
This will output `"Hello world"` with a space between the words. The `nl` parameter can be used for a new line. For example:
```
print("Hello", "nl")
print("World", "nl")
```
## Lists
Altern8 supports basic list functionalities like adding an element, removing an element, extending another list, and finding the length of a list. To access an element of a list, use the index value followed by the `@` symbol. For example: `print(l @ 0, "nl")`, which returns the value of the `0th` index value, i.e., `1`.

An element can be added to the list using the `append()` function or the `+` symbol. For example:
```
append(l, 6) # add 6 to the list l
l + 6 # same as append function
```
An element can be removed from the list using the `pop()` function or the `-` symbol. For example:
```
pop(l, 6) # remove 6 from the list l
l - 6 # same as pop function
```
To extend a list to another list, use the `extend()` function or the `*` symbol. For example:
```
extend(l1, l2) # extend list l2 to the list l1
l1 * l2 # same as extend function
```
To find the length of a list, use the `len()` function. For example: `print(len(l), "nl")`, which outputs the length of the list `l`.

## Strings
To concatenate two strings in Altern8, use the `+` symbol. To embed the value of a variable into a string, use `{}`. For example:
```
var num = 5
print("The number is : { num }", "nl") # outputs "The number is : 5"
```
If the variable is not declared, it prints the same string, i.e., `"The number is : { num }"`.

## For Loops
A for loop can have a single statement without a new line. For example:
`for i = 1 to 6 then print(i, ",")`

This will print 1, 2, 3, 4, 5. The `step` value can be used to jump values. For example:
`for i = 1 to 6 step 2 then print(i, ",")`

This will print 1, 3, 5. The `break` and `continue` keywords can also be used in a for loop.

## While Loop
A while loop can be used to loop the block of statements for a given number of times. For example:

```
var i = 0
while i < 6 then
    $sum = sum + i
    $i = i + 1
end
print(sum, "nl")
```
This will run the loop from 1 to 5 and print 15. The break and continue keywords can also be used in a while loop.

## If Statement
The `if` statement in Altern8 is used to run the block of statements if the condition is true. For example:

```
if 1 < 5 then
    print("Hello", "nl") # outputs "Hello"
end
```
The `elif` keyword can be used to check multiple conditions. Multiple `elif` statements can also be used. For example:

```
if 2 > 5 then
    print("Hello", "nl")
elif 5 < 7 then
    print("world", "nl") # outputs "world"
end
```
The `else` keyword can be used to run a block of code if the given conditions are false. For example:

```
if 2 > 5 then
    print("Hello", "nl")
else
    print("world", "nl")
end # outputs "world"
```

## Functions
Functions in Altern8 can be used to write a block of statements once and can be used many number of times. The define keyword is used for function declaration. A single line statement can be used with the -> symbol. For example:

```
define sum(a, b) -> return a + b
sum(1,2) # outputs 3
sum(3,4) # outputs 7
```
Multi-line statements can be used with the `end` keyword. For example:

```
define num(a, b)
    print(a+b, ",")
    print(a*b, "nl")
end
num(2,3) # outputs 5,6
```
Anonymous functions can also be used and assigned to a variable. For example:

```
var sum = func(a, b) -> return a + b
print(sum, "nl") # outputs <anonymous function>
print(sum(1,2), "nl") # outputs 3
```
The `is_func()` function returns true if the element passed to it is a function.

