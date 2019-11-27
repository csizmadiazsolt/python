#!/usr/bin/python3

word = str(input("Enter a word: "))
word_length = len(word)
is_palindrome = 1

for i in range(0,int(word_length/2)):
  if(word[i] != word[word_length-1-i]):
    is_palindrome = 0
    break

if is_palindrome == 1:
  print("This word is a palindrome.")
else:
  print("This word is not a palindrome.")