# Talks about different data-types
#broader category "Mutability" & "immutability" datatypes
#strings, numbers, booleans, lists, sets, frozensets, tuples, ranges, dictionaries, none
#mutable - data can be modified after creation (list, sets, dictionaries)
#immutable - data can't be modified after creation (strings, numbers, tuples, frozensets)

# tuples can be called as immutable lists

Most commonly used string methods

index, count, find, upper, lower, startswith, endswith, strip, replace, split & join

String Method: Index - shows the first occurance index id in any given string
Example:
>>> a = "ajaz ahmed"
>>> a.index("a")
0
>>> a.index("i")
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a.index("i")
ValueError: substring not found

String method: Count - to get the number of occurances for any given character in a mentioned string
Example:
>>> a.count("a")
3

String Method: Find - to get the starting index id of a character set
>>> a.find("jaz")
1
>>> a.find("abc")
-1

String Method: Upper / Lower - to change case of any given character
>>> a.upper()
'AJAZ AHMED'
>>> a
'ajaz ahmed'

String Method: startswith / endswith - boolean answer to find out if mentioned character is found in the string
>>> a.startswith("a")
True
>>> a.endswith("d")
True
>>> a.endswith("a")
False

String Method: 
Strip - 
Replace - 
Split -
Join -

>>> b = "    ajaz ahmed    "
>>> b.strip()
'ajaz ahmed'
>>> b.replace(" ", "")
'ajazahmed'
>>> d = "$$$ajaz ahmed$$$"
>>> d.strip("$")
'ajaz ahmed'
>>> e = "ajaz, ahmed, sonu, mithu"
>>> e.split(",")
['ajaz', ' ahmed', ' sonu', ' mithu']
>>> my_string = "a0:12:90:00:80:43"
>>> my_string.split(':')
['a0', '12', '90', '00', '80', '43']
>>> a
'ajaz ahmed'
>>> "_".(a)
SyntaxError: invalid syntax
>>> "_".join(a)
'a_j_a_z_ _a_h_m_e_d'
