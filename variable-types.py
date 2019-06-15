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
print("list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]\t\t\t\t# Declare a List\ntinylist = [123, 'john']\t\t\t\t\t\t# Declare a Tinylist")
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
# Prints complete list
print("print(list):",end=' ')
print(list, end=' ')
print("\t\t\t\t# Prints complete list")
# Prints first element of the list
print("print(list[0]):",end=' ')
print(list[0],end=' ')
print("\t\t\t\t\t\t\t# Prints first element of the list")
# Prints elements starting from 2nd till 3rd
print("print(list[1:3]):", end=' ')
print(list[1:3], end=' ')
print("\t\t\t\t\t\t# Prints elements starting from 2nd till 3rd")
# Prints elements starting from 3rd element
print("print(list[2:]):",end=' ')
print(list[2:], end=' ')
print("\t\t\t\t\t# Prints elements starting from 3rd element")
# Prints list two times
print("print(tinylist*2):",end=' ')
print(tinylist*2, end=' ')
print("\t\t\t\t# Prints list two times") 
# Prints concatenated lists
print("print(list + tinylist)", end=' ')
print(list + tinylist, end=' ')
print("\t# Prints concatenated lists")
''' Python Tuples '''
print("------------------------------------------------------------------------------------------------------\nPython Tuples\n---")
# Declare Tuples
print("tuple = ('abcd', 786 , 2.23, 'john', 70.2)\t\t\t\t\t# Declare Tuple \ntinytuple = (123, 'john')\t\t\t\t\t\t\t# Declare a Tinytuple")
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')
# Prints complete tuple
print("print(tuple):", end=' ')
print(tuple, end=' ')
print("\t\t\t\t# Prints complete tuple")
# Prints first element of the tuple
print("print(tuple[0]):",end=' ')         
print(tuple[0], end=' ')        
print("\t\t\t\t\t\t\t\t# Prints first element of the tuple")
# Prints elements starting from 2nd till 3rd
print("print(tuple[1:3]):",end=' ')
print(tuple[1:3], end=' ')
print("\t\t\t\t\t\t\t# Prints elements starting from 2nd till 3rd ")
# Prints elements starting from 3rd element
print("print(tuple[2:])",end=' ')
print(tuple[2:], end=' ')
print("\t\t\t\t\t\t# Prints elements starting from 3rd element")
# Prints tuple two times
print("print(tinytuple*2)",end=' ')
print(tinytuple * 2, end=' ')   
print("\t\t\t\t\t# Prints tuple two times")
# Prints concatenated tuple
print("print(tuple + tinytuple):", end=' ')
print(tuple + tinytuple, end=' ') 
print("\t# Prints concatenated tuple")















