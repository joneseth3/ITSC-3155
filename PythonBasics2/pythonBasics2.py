# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

from array import array
from re import A


def count_threes(n):
  j = 0

  for x in range(0,n):
    if x % 3 == 0:
      j += 1
    else:
      continue
  return j


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  max_count = 0
  max_char = None
  prev_char = None

  for current in s:
    if prev_char == current:
      count += 1
    else: 
      count = 1
    if count > max_count:
      max_count = count
      max_char = current
    prev_char = current
  
  return max_char


# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
  lower_s = s.lower()
  lower_s = lower_s.replace(" ", "")

  word = lower_s[::-1]
  
  if lower_s == word:
    return True 
  else:
    return False









