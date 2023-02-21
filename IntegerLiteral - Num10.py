#Programming Language Concepts
#Exam 1 Question 10
#Nick Conn

import re

# Regular Expression pattern to check if a string is an integer literal
pattern =  "(0[xX][0-9a-fA-F]+)(I64)?(Ui64)?|(0[0-7]+[ul]?)|([0-9]+[ul]?)$"
 
testStrings = ['28', '4000000024u', '2000000022l', '04000000024u', '02000000022l', '0x4a44000000000020I64', '0x8a44000000000040Ui64', '0x2a', 'test123', '123124asd']

for num in testStrings:
    result = re.match(pattern, num)

    if result:
        print(num, "is an integer literal.")
    else:
        print(num, "is not an integer literal.")