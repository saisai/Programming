#!/usr/bin/env python

"""
Exercise 1:
Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if-then-else construct available in Python. (It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)
"""

def max_num(n1 , n2):
	"Returns the largest of two numbers"
	if n1 > n2:
		return n1
	elif n2 > n1:
		return n2
	else:
		return n1
		
def max_of_three(a, b, c):
	"Returns the largest of three numbers"
	return max_num( max_num(a,b) ,c)
	
def length(l_list):
	"Returns the length of a list or string"
	
	count = 0
	for i in l_list:
		count+= 1
	
	return count
	
def is_vowel(ch):
	"Return true if a char is a vowel"
	vowels = ['a', 'e', 'i', 'o', 'u']
	
	if len(ch) > 1:
		return False
	
	if ch in vowels:
		return True
	else:
		return False
	
def translate(str):
	
	tmp = ""
	for let in str:
		if not is_vowel(let):
			tmp += let + "o" + let
		else:
			tmp += let
			
	return tmp
			
def sum(list):
	"Returns the sum of all numbers in the list"
	sum = 0
	for n in list:
		sum += n
		
	return sum
	
def multiply(list):
	"Returns the product of all numbers in the list"
	prod = 1
	for n in list:
		prod *= n

	return prod

def reverse(str):
	"Returns a string reversed"
	tmp = ""
	l_rev = []
	
	for i in range(0,len(str)):
		l_rev.insert(0,str[i: i+1])
		
	for c in l_rev:
		tmp += c
		
	return tmp

def is_palindrome(word):
	"Returns True is a word is the same written backwards"
	
	r_word = reverse(word)
	
	if r_word == word:
		return True
	else:
		return False
	
def is_member(x, l_list):
	"Return True if x is a member of the list"
	
	for i in l_list:
		if x == i:
			return True
	
	return False

def overlapping(l_a, l_b):
	"Returns true if both list have at least one member in common"
	
	for item in l_a:
		
		if is_member(item, l_b):
			return True
		
	return False
	
def generate_n_chars(n ,ch):
	"Returns a string that is n long, with char ch"
	
	if n == 0 or n <= 0:
		return None
		
	tmp = ""
	for i in range(0, n):
		tmp += ch
		
	return tmp
	
def histogram(l_ints):
	"Takes a list of ints and prints a histogram to the screen"
	
	for n in l_ints:
		print generate_n_chars(n,'*')

def max_in_list(l_list):
	"Returns the largest number in the list"
	
	for i in l_list:
		max = i
		for j in l_list:
			if j >= max:
				max = j
	
	return max

def map_word_to_length(word_list):
	"maps a list of words into a list of integers representing the lengths of the correponding words."
	
	len_list = []
	
	for word in word_list:
		len_list.append(len(word))
		
	return len_list

def find_longest_word(word_list):
	"Returns the length of the longest word in the list"
	return max_in_list(map_word_to_length(word_list))
	
def filter_long_words(word_list, n):
	"Returns a list of words that are longer than n"
	
	ln = map_word_to_length(word_list)
	l_long_words = []
	
	for w in range(0, len(ln)):
		
		if ln[w] > n:
			l_long_words.append(word_list[w])
	
	return l_long_words
	
	
	
### MAIN PROGRAM ###
# print max_of_three(1,2,3)
# print max_of_three(5,2,-1)
# print length("Gawaine O'Gilvie")
# print length([5,5,8,9])
# print is_vowel('z')
# print is_vowel('a')
# print translate("this is fun")
# print sum([1,2,3,4])
# print multiply([1,2,3,4])
# print reverse("I am testing")
# print is_palindrome("radar") 
# print is_member(27, [3,5,6,78,45,6])
# print overlapping([1,2,10,4], [10,5,6,7])
# print generate_n_chars(10, '*')
# histogram([1,2,3,4,5,6,7,8,9,10])
# print max_in_list([1,103,3,-256,1,5,65,102,26])
# print find_longest_word(['ROTAVATOR ', 'ABSTENTIOUS', 'car', 'banana', 'SUBDERMATOGLYPHIC'])
# print filter_long_words(['dog','apple','cat', 'pizza'], 3)
