import sys
############################################################## Python Variables ###
print("----------------------\nPython variables\n---")
counter = 100
miles = 1000.0
name = "John"
print("counter: ", counter)
print("miles: ", miles)
print("name: ", name)
############################################################## Python Strings ###
print("----------------------\nPython Strings\n---")
print("str = 'Hello World!'")
str = 'Hello World!'
print("print(str):\t\t" 		+ str + 			"\t\t\t# Prints complete string")
print("print(str[0]): \t\t" 	+ str[0] + 			"\t\t\t\t# Prints first character of the string")
print("print(str[2:5]) \t" 		+ str[2:5] + 		"\t\t\t\t# Prints characters starting from 3rd to 5th")
print("print(str[2:]): \t" 		+ str[2:] + 		"\t\t\t# Prints string starting from 3rd character")
print("print(str * 2): \t" 		+ str * 2 + 		"\t# Prints string two times")
print('print(str + "TEST"): \t' + str + 'TEST' + 	'\t\t# Prints concatenated string')
############################################################## Python Strings ###
print("----------------------\nPython Lists\n---")
print("list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]\ntinylist = [123, 'john']")
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print("print(list): # Prints complete list")
print(list)
print("print(list[0]): # Prints first element of the list")
print(list[0])
print("print(list[1:3]): # Prints elements starting from 2nd till 3rd")
print(list[1:3])
print("print(list[2:]): # Prints elements starting from 3rd element")
print(list[1:3])
print("print(tinylist*2): # Prints list two times") 
print(tinylist*2)
print("print(list + tinylist) # Prints concatenated lists")
print(list + tinylist)