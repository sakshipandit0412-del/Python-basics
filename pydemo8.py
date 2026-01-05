courses = ['ba', 'bcom', 'bsc', 'be']

for course in courses:
    print(course)
    
    fruits = ('apple', 'banana', 'mango')

for fruit in fruits:
    print(fruit)
    
company = {'name': 'Tesla', 'founder':'Elon', 'year': 2003}

for item in company:
    print(item, company[item])
    
text = 'Hello'
for i in text:
  print(i)
  
for i in range(5):   # prints from 0 to 4
  print(i)

print('------------')

for i in range(3,8):   # prints from 3 to 7
  print(i)
  
courses = ['ba', 'bcom', 'bsc', 'be']
for id, item in enumerate(courses):
  print(id, item)
  
courses = ['ba', 'bcom', 'bsc', 'be']

for course in courses:
    if course == 'bcom':
        print(course)
    else:
        print('Course is NOT bcom')
        
courses = ['ba', 'bcom', 'bsc', 'be']
for item in courses:
  print(item)
  if item == 'bsc':              
    break           

courses = ['ba', 'bcom', 'bsc', 'be']
for course in courses:
  if course == 'bsc':
    continue
  print(course) 