#!/usr/bin/env python3

concat = __import__('1-concat').concat

str1 = "egg"
str2 = "shell"
# This will print True if the function works correctly
print(concat(str1, str2) == "{}{}".format(str1, str2))
# This will print the type annotations of the function
print(concat.__annotations__) 
