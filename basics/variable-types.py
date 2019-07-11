import sys
''' Python Variables '''
print("------------------------------------------------------------------------------------------------------\nPython variables\n---")
counter = 100
miles = 1000.0
name = "John"
print("counter: \t", counter)
print("miles: \t\t", miles)
print("name: \t\t", name)
''' Python Strings '''
print("------------------------------------------------------------------------------------------------------\nPython Strings\n---")
print("str = 'Hello World!'")
str = 'Hello World!'
print("print(str):\t\t" 		+ str + 			"\t\t\t# Prints complete string")
print("print(str[0]): \t\t" 	+ str[0] + 			"\t\t\t\t# Prints first character of the string")
print("print(str[2:5]) \t" 		+ str[2:5] + 		"\t\t\t\t# Prints characters starting from 3rd to 5th")
print("print(str[2:]): \t" 		+ str[2:] + 		"\t\t\t# Prints string starting from 3rd character")
print("print(str * 2): \t" 		+ str * 2 + 		"\t# Prints string two times")
print('print(str + "TEST"): \t' + str + 'TEST' + 	'\t\t# Prints concatenated string')
''' Python Lists '''
print("------------------------------------------------------------------------------------------------------\nPython Lists\n---")
# Declare Lists
print("list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]\t\t\t\t\t# Declare a List\ntinylist = [123, 'john']\t\t\t\t\t\t\t# Declare a Tinylist")
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
# Prints complete list
print("print(list):\t\t",end=' ')
print(list, end=' ')
print("\t\t\t# Prints complete list")
# Prints first element of the list
print("print(list[0]):\t\t",end=' ')
print(list[0],end=' ')
print("\t\t\t\t\t\t\t# Prints first element of the list")
# Prints elements starting from 2nd till 3rd
print("print(list[1:3]):\t", end=' ')
print(list[1:3], end=' ')
print("\t\t\t\t\t\t# Prints elements starting from 2nd till 3rd")
# Prints elements starting from 3rd element
print("print(list[2:]):\t",end=' ')
print(list[2:], end=' ')
print("\t\t\t\t\t# Prints elements starting from 3rd element")
# Prints list two times
print("print(tinylist*2):\t",end=' ')
print(tinylist*2, end=' ')
print("\t\t\t\t# Prints list two times") 
# Prints concatenated lists
print("print(list + tinylist):\t", end=' ')
print(list + tinylist, end=' ')
print("\t# Prints concatenated lists")
''' Python Tuples '''
print("------------------------------------------------------------------------------------------------------\nPython Tuples\n---")
# Declare Tuples
print("tuple = ('abcd', 786 , 2.23, 'john', 70.2)\t\t\t\t\t\t# Declare Tuple \ntinytuple = (123, 'john')\t\t\t\t\t\t\t\t# Declare a Tinytuple")
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')
# Prints complete tuple
print("print(tuple):\t\t\t", end=' ')
print(tuple, end=' ')
print("\t\t\t# Prints complete tuple")
# Prints first element of the tuple
print("print(tuple[0]):\t\t",end=' ')         
print(tuple[0], end=' ')        
print("\t\t\t\t\t\t\t# Prints first element of the tuple")
# Prints elements starting from 2nd till 3rd
print("print(tuple[1:3]):\t\t",end=' ')
print(tuple[1:3], end=' ')
print("\t\t\t\t\t\t# Prints elements starting from 2nd till 3rd ")
# Prints elements starting from 3rd element
print("print(tuple[2:]):\t\t",end=' ')
print(tuple[2:], end=' ')
print("\t\t\t\t\t# Prints elements starting from 3rd element")
# Prints tuple two times
print("print(tinytuple*2):\t\t",end=' ')
print(tinytuple * 2, end=' ')   
print("\t\t\t\t# Prints tuple two times")
# Prints concatenated tuple
print("print(tuple + tinytuple):\t", end=' ')
print(tuple + tinytuple, end=' ') 
print("\t# Prints concatenated tuple")
''' Python Dictionary '''
print("------------------------------------------------------------------------------------------------------\nPython Dictionary\n---")
# Declare Dictionary
print("dict = {}\t\t\t\t\t\t\t\t\t\t# Declare Dictionary 1\ndict['one'] = 'This is one'\t\t\t\t\t\t\t\t# Declare Dictionary 2\ndict[2] = 'This is two'\t\t\t\t\t\t\t\t\t# Declare Dictionary 3\ntinydict = {'name': 'john','code':6734, 'dept': 'sales'}\t\t\t\t# Declare tinydict")
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
# Prints value for 'one' key
print("print(dict['one']):\t\t", end=' ')
print(dict['one'], end=' ')
print("\t\t\t\t\t\t# Prints value for 'one' key")
# Prints value for 2 key
print("print(dict[2]):\t\t\t", end=' ')
print(dict[2], end=' ')           
print("\t\t\t\t\t\t# Prints value for 2 key")
# Prints complete dictionary
print("print(tinydict):\t\t", end=' ')
print(tinydict, end=' ')          
print("\t# Prints complete dictionary")
# Prints all the keys
print("print(tinydict.keys()):\t\t", end=' ')
print(tinydict.keys(), end=' ')   
print("\t\t\t# Prints all the keys")
# Prints all the values
print("print(tinydict.values()):\t", end=' ')
print(tinydict.values(), end=' ') 
print("\t\t\t# Prints all the values")
''' Python Data Type Conversion '''
print("------------------------------------------------------------------------------------------------------\nPython Data Type Conversion\n---")
print("refer to https://www.tutorialspoint.com/python3/python_variable_types.htm")





































