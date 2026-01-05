company = {
  "name": "Tesla",              # this is called dictionary iteam. This dictionary has 3 items. 
  "founder": 'Elon Musk',
  "established": 2003
}
print(company)

print(type(company))

print(company['name'])


print(len(company)) 

company['name'] = 'TESLAA'
print(company)

company['location'] = 'US'
print(company)

print(company.get('name'))   
print(company.get('namee'))

print(company.keys())
print(company.values())

company['newkey'] = 'newval'
print(company.keys())
print(company.values())

student = {
    'name' : 'John',
    'age' : 12,
    'class' : 7
}

print(student)

student.pop('class')   
print(student)

student = {
    'name' : 'John',
    'age' : 12,
    'class' : 7
}

print(student)

del student['class']     
print(student)

student = {
    'name' : 'John',
    'age' : 12,
    'class' : 7
}

print(student)
student.clear()
print(student)

new = dict({'name': 'Apple', 'year': 1975, 'founder': 'Steve Jobs and Steve Wozniak'})     # dict is special keyword, wrap your dictionary within dict() 

print(new)
print(type(new))

for item in new:              
  print(item)
  
for item in new:           
  print(item, new[item])   
  
for item, val in new.items():
  print(item, val)
  
for key in new.keys():
  print(key)
  
for key in sorted(new):     
  print(key)  
  
  company = {
    'name': 'Apple',
    'year': 1975,
    'founders': {
        'first': 'Steve Jobs',
        'second': 'Steve Wozniak'
    }
    }
print(company)

print(company['founders'])
print(company['founders']['first'])

for item, val in company.items():
  print(item, val)
  
  print(type(company['founders']))