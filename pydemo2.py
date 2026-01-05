courses = ['ba', 'bcom', 'bsc', 'ma', 'mcom', 'msc']
print(courses) 

print(type(courses))

print(courses[0])
print(courses[0:2])

print(courses[1:5])

print(courses[-3:-1])


courses.append('BE')
print(courses)

courses.insert(3, 'ME')          
print(courses)

new = ['11th', '12th']  
courses.append(new)      
print(courses)  

courses.extend(new)
print(courses)

courses.pop()
print(courses)

fruits = ['mango', 'apple', 'orange', 'kiwi', 'pineapple', 'papaya']
print(fruits)

fruits.sort()
print(fruits)

 
fruits.reverse()
print(fruits) 

print(len('HELLO'))

countries = ['Russia', 'India', 'US', 'Japan', 'Germany', 'Italy', 'Zambia']

print(max(countries))   
print(min(countries))



for item in countries:            # item could be changed by any other random name. 
  print(item)
  
  for x in countries:
      print(x)
print('Now I am outside the for loop')

print('-------------')

for x in countries:
  print(x)
  print('Now I am inside the for loop')

for item in countries:
  print(item, len(item))     