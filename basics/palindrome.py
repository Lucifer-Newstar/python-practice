##this is a program to check if a string is palindrome. i.e the string is same even if reveresed
import string

input_word = input("Enter the word: ")
##to remove punctuation and spaces from the word
clear_word = "".join(char.lower() for char in input_word if char not in string.punctuation and char != " ")

backward = clear_word[::-1]

if clear_word == backward:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")
