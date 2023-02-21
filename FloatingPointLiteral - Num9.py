#Programming Language Concepts
#Exam 1 Question 9
#Nick Conn

import re

# Regular Expression pattern to check if a string is a floating point literal
pattern =  "[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?([fFlL])?$"
 
testStrings = ['15.75L', '1.575E1', '1575e-2', '-2.5e-3F', '25E-4', '123E', 'test123']

for num in testStrings:
    result = re.match(pattern, num)

    if result:
        print(num, "is a floating point literal.")
    else:
        print(num, "is not a floating point literal.")