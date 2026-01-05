courses = ('ba', 'bcom', 'bsc')
print(courses)
print(type(courses)) 


print(courses[1])

print(courses.count('ba'))
print(courses.count('baa'))

courses = ('ba', 'bcom', 'bsc', 'bsc', 'ba')
print(courses)
print(courses.count('bsc'))           
print(courses.index('bsc'))  

for item in courses:     
  print(item)
  
  nums = (2, 3, 4)
print(type(nums))

data = ('ba', 2, True, 'bsc')
print(data)
print(type(data))

print(type(data[0]))
print(type(data[1]))

new = ('50')              
print(type(new))

print('-----------------------------')

new1 = ('50',)            
print(type(new1))

print(('a','b','c') + (1, 2, 3))

new = ('50',)
new1 = ('apple',)
new2 = ('mango','orange')
print(new + new1 + new2)

fruits = ('apple','mango')

print('mango' in fruits)   
print('mangoes' in fruits)

print(max(2, 1, 3, 7))
print(min(2, 1, 3, 7))

num = [1, 2, 3, 4]
new = tuple(num)

print(num)
print(new)

num = (1, 2, 3, 4, 5, 6, 7)
print(num[-1])
print(num[-2])

courses = ('ba', 'bcom', 'bsc', 'be', 'ma', 'mcom',' msc', 'me')
print(courses[3:5])  
print(courses[3:]) 
print(courses[:3]) 
print(courses[-3:])

#i am hear 