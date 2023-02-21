#Programming Language Concepts
#Exam 1 Question 8
#Nick Conn

import re

# Regular Expression pattern to check if a string is an Email
pattern =  "[a-zA-Z0-9#!%$‘&+*–/=?^_`{|}~]+(\.[a-zA-Z0-9#!%$'&+*–/=?^_`{|}~]+)*"
 
testStrings = ['a1@gmail.com', 'a-b@c.gov', '-a@gov.com', 'apple@site.com-', 'test1233-31@big-site.com']

for email in testStrings:
    result = re.match(pattern, email)

    if result:
        print(email, "is a valid email address.")
    else:
        print(email, "is not a valid email address.")