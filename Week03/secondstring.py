# secondstring.py
# Code that takes input sentence and outputs every second letter in reverse order.
# Author: Liam Nutley
word=(input("Enter Sentence: "))
str = word
stringlength=len(str)
slicedString=str[stringlength::-1]
print(slicedString[::2])