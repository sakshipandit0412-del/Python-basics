num1 = 3
num2 = 5
print(num1, num2)
print(type(num1), type(num2))

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num2 / num1)

print(num2 // num1)  
print(num2 % num1)   
print(3 ** 2)    

print(9 // 3)
print(8 // 3)
print(7 // 3)
print(6 // 3)

print(9 % 3)
print(8 % 3)
print(7 % 3)
print(6 % 3)

print(5 * 4 + 1)         
print(1 + 5 * 4)          
print(5 * (4 + 1) ) 

print(2 == 2)   
print(2 == 1) 

print(3 != 2)
print(3 > 2)
print(3 < 2)
print(3 >= 3)
print(3 >= 2) 
print(3 <= 2)

num = 4
print(num)

num += 1  
print(num)

num = 4
print(num)

num -= 1   # is equivalent to num = num - 1
print(num) 

num = 4
num /= 2
print(num)

print(True and True)
print(True and False)   # same as False and True
print(False & False)  

print(True or True)   
print(True or False)
print(False | False)  

print(not True)
print(not False)

x = 5
print(x > 4 and x < 6)
x = 5
print(x > 3 or x < 4) 
x = 5
print(not(x > 3 and x < 10))

print(abs(-2))
print(abs(-2.1))
print(round(3.45))
print(round(-3.95))

print(round(3.46, 1))   
print(round(3.46, 2))   

print(round(3.469, 1))   
print(round(3.469, 2))  

new1 = 2.1
new2 = 0.3

print(new1 + new2)
print(new1 - new2)

fir = 3 
sec = 0.1  
print (fir + sec)

num1 = 'Hello'
num2 = '5'
print(num1 + num2)

a = '2'
b = '3'
print(a, type(a))
print(b, type(b))
print('Addition = ', a+b)   

print()                    

a = int(a)
b = int(b)
print(a, type(a))       
print(b, type(b))       
print('Addition = ', a+b)
"""
y= 'hi'
y = int(y)    
print(a) 
"""

num = 2.0
print(type(num))
num = str(num)
print(type(num))

num = 'True'
print(type(num))
num = bool(num)
print(type(num))

num = input('enter some integer  -  ')   # pass some number e.g. 2
print(num)
print(type(num))

num = input('Enter some number --- ')     # pass some number e.g. 2   
print(num, type(num))
new = int(num)            # this is called typecasting (i.e. you are changing data type of variable) (this line will give you error if you pass some text in the input box, try it!)
print(new, type(new))

num1 = input('Enter first number:  ')
num2 = input('Enter second number:  ')
print(num1 + num2)    # this will simply append the two numbers one after the other
print(int(num1) + int(num2)) 


x = 7
if x > 10:
    print('x is greater than 10')
    if x > 20:
        print('x is greater than 20')
        if x > 30:
            print('x is greater than 30')
        else:
            print('x is smaller than 30')
    else:
        print('x is smaller than 20')
else:
    print('x is smaller than 10')
    
    x = int(input("Enter any number within range 10: "))     # if you pass anything other than integer, it'll throw error. Because we are typecasting here itself
print(x >= 3 and x <= 10)