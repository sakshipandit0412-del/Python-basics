print("Code for hello world.")
demo = "Hello world!"
print(demo)
print(type(demo))

print("Introduction to number.")
num = 3
another_num = 3.0
print(type(num))
print(type(another_num))

print("introduction to boolean value.")
val = True
print(type(val))

print("Print all.")
print(num)
print(another_num)
print(val)

print("Types of numbers.")
num1 = 3
num2 = 5
print(num1, num2)
print(type(num1), type(num2))

print("operations on numbers.")
print(num1-num2)
print(num1*num2)
print(num2 / num1)   
print(num2 // num1)  
print(num2 % num1) 

print("Operations on float.")
new1 = 2.1
new2 = 0.3
print(new1 + new2)
print(new1 - new2)
"""
print("Take input from user.")
name = input('enter your name')   # once this is run, type anything in the box
print(name)
print(type(name))
"""

print("Operations on strings.")
text = input('Enter some text    ->')    # Pass any text
print("String in upper-",text.upper())
print("Print tittle-",text.title())
print("Find alphabet-",text.find('e'))
print("Count letters-",text.count('e'))
print("Replace text-",text.replace('e','z'))
print("Find text-",len(text))

str="mystring"
help(str) 
dir(str)
