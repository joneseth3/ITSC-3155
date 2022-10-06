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
	n = list(str(n)) #turns string into list 
	dic ={}

	dic[3] = dic[6] = dic[9] = 0  #since we only are checking single digit numbers, I set the 3/div numbers to 0 in the dict
	
	for i in n:  #runs through the list an pulls number to dict that are 3/div and counts the occurences 
		j = int(i)
		if j % 3 == 0 and j != 0:
			dic[j] = dic[j] + 1


	max = -1
	index = -1
	for i,j in dic.items():    #checks the biggest numbers and then returns for answer 
		if j > max:
			max = j
			index = i

	return index


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  s = list(s)   #turns string into list 
  list_length = len(s)
  count = 1

  dic = {}
  for i in range(0, list_length -1):   #runs through the list and pulls chars into dic and counts occurences 
    if(s[i] != s[i+1]):
      if((s[i] in dic) and dic[s[i]] > count):
        continue
      else:
        dic[s[i]] = count
        count = 1
    else:
      count = count + 1

  dic[s[list_length -1]] = count

  max = -1    #checks the chars that occur the most and then returns for answer
  for i,j in dic.items():
    if j > max:
      max = j
  
  lst = []
  for i,j in dic.items():
    if j == max:
      lst.append(i)

  return lst


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









