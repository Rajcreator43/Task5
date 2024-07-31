#Variables
# x=1
# y=2.5
# name="Raj"
# _is=True

# x,y,name,_is=(1,2.5,"Raj",True)

# a=x+y
# print(x,y,name,_is)
# print(a)
# a=str(a)
# print(type(a))


# strings

name="Raj"
age=18

# print(f"My name is {name} and my age is {age}")
# print("My name is {name} and my age is {age}".format(name=name,age=age))
# print("My name is "+name+" and my age is "+ str(age))

# String Methods

# s = 'helloworld'

# # Capitalize string
# print(s.capitalize())

# # Make all uppercase
# print(s.upper())

# # Make all lower
# print(s.lower())

# # Swap case
# print(s.swapcase())

# # Get length
# print(len(s))

# # Replace
# print(s.replace('world', 'everyone'))

# # Count
# sub = 'h'
# print(s.count(sub))

# # Starts with
# print(s.startswith('hello'))

# # Ends with
# print(s.endswith('d'))

# # Split into a list
# print(s.split())

# # Find position
# print(s.find('r'))

# # Is all alphanumeric
# print(s.isalnum())

# # Is all alphabetic
# print(s.isalpha())

# # Is all numeric
# print(s.isnumeric())

# list


# A List is a collection which is ordered and changeable. Allows duplicate members.

# # Create list
# numbers = [1, 2, 3, 4, 5]
# fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# # Use a constructor
# # numbers2 = list((1, 2, 3, 4, 5))

# print(fruits[1])


# print(fruits[-1])



# # Get length
# print(len(fruits))

# # Append to list
# fruits.append('Mangos')

# # Remove from list
# fruits.remove('Grapes')

# # Insert into position
# fruits.insert(2, 'Strawberries')

# # Change value
# fruits[0] = 'Blueberries'

# # Remove with pop
# fruits.pop(2)

# # Reverse list
# fruits.reverse()

# # Sort list
# fruits.sort()

# # Reverse sort
# fruits.sort(reverse=True)

# print(fruits)

# tuples

# fruits=("A","B","C","D")
# fruits2=tuple(("A","B","C","D"))
# print(fruits,fruits2)
# fruits2=("A",)
# print(type(fruits2))
# fruits[0]="P"
# del fruits2
# print(len(fruits))

# set

# fruits_set = {'Apples', 'Oranges', 'Mango'}

# # Check if in set
# print('Apples' in fruits_set)

# # Add to set
# fruits_set.add('Grape')

# # Remove from set
# fruits_set.remove('Grape')

# # Add duplicate
# fruits_set.add('Apples')

# # Clear set
# fruits_set.clear()

# # Delete
# del fruits_set

# print(fruits_set)


# dictionary

# person = {
#     'first_name': 'John',
#     'last_name': 'Doe',
#     'age': 30
# }
# person2 = dict(first_name='Sara', last_name='Williams')

# print(person['first_name'])
# print(person.get('first_name'))

# person['phone']= 12345789

# print(person)

# print(person.keys())
# print(person.items())
# person2=person.copy()
# person2['city']="Mumbai"
# print(person2)

# del(person['age'])
# person.clear()
# print(len(person2))
# print(person)

# people = [
#     {'name': 'Martha', 'age': 30},
#     {'name': 'Kevin', 'age': 25}
# ]

# print(people[0]['name'])


# function 

# def sayHello(name='Sam'):
#     print(f"Hello {name}")
# sayHello("Raj")

# def getSum(num1,num2):
#     total=num1+num2
#     return total  
# print(getSum(4,5))

# getSum=lambda num1, num2: num1+num2
# print(getSum(1,38))

# x = 21
# y = 20

# # Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# # Simple if
# if x > y:
#   print(f'{x} is greater than {y}')

# # If/else
# if x > y:
#   print(f'{x} is greater than {y}')
# else:
#   print(f'{y} is greater than {x}')  

# # elif
# if x > y:
#   print(f'{x} is greater than {y}')
# elif x == y:
#   print(f'{x} is equal to {y}')  
# else:
#   print(f'{y} is greater than {x}')  

# # Nested if
# if x > 2:
#   if x <= 10:
#     print(f'{x} is greater than 2 and less than or equal to 10')
    

# # Logical operators (and, or, not) - Used to combine conditional statements

# # and
# if x > 2 and x <= 10:
#     print(f'{x} is greater than 2 and less than or equal to 10')

# # or
# if x > 2 or x <= 10:
#     print(f'{x} is greater than 2 or less than or equal to 10')

# # not
# if not(x == y):
#   print(f'{x} is not equal to {y}')


# # Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

# numbers = [1,2,3,4,5]

# #  in
# if x in numbers:
#   print(x in numbers)

# # not in
# if x not in numbers:
#   print(x not in numbers)

# # Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# # is
# if x is y:
#   print(x is y)

# # is not
# if x is not y:
#   print(x is not y)

# loops 
people=["Raj","Harsh","Gad","Manan"]

# for i in people :
#     print(f'Hello {i}')

# for i in people :
#     if i=="Gad":
#         break
#     print(f'Hello {i}')

# for i in people :
#     if i=="Gad":
#         continue
#     print(f'Hello {i}')

# for i in range(0,11):
#     print(f'Number : {i}')

# c=0
# while c<=10:
#     print(f'{c}')
#     c+=1


# import datetime
# from datetime import date
# today=date.today()
# print(today)

# import time
# from time import time
# t=time()
# print(t)

# import validator
# from validator import validate_email

# email="vadapav#gmail.com"

# if validate_email(email):
#     print("Email acha hai ")
# else:
#     print("Faltu email hai")

# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
# class User:

#   # Constructor
#   def __init__(self, name, email, age):
#     self.name = name
#     self.email = email
#     self.age = age
    

#   def greeting(self):
#       return f'My name is {self.name} and I am {self.age}'


# Extend class
# class Customer(User):
#   # Constructor
#   def __init__(self, name, email, age):
#       User.__init__(self, name, email, age) #Called proper parent class constructor to make this as proper child inehriting all methods.
#       self.name = name
#       self.email = email
#       self.age = age
#       self.balance = 0

#   def set_balance(self, balance):
#       self.balance = balance

#   def greeting(self):
#       return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

# #  Init user object
# brad = User('Brad Traversy', 'brad@gmail.com', 37)
# # Init customer object
# janet = Customer('Janet Johnson', 'janet@yahoo.com', 25)

# janet.set_balance(500)
# print(janet.greeting())


# Python has functions for creating, reading, updating, and deleting files.

# Open a file
# myFile = open('myfile.txt', 'w')

# # Get some info
# print('Name: ', myFile.name)
# print('Is Closed : ', myFile.closed)
# print('Opening Mode: ', myFile.mode)

# # Write to file
# myFile.write('I love Python')
# myFile.write(' and JavaScript')
# myFile.close()

# # Append to file
# myFile = open('myfile.txt', 'a')
# myFile.write(' I also like PHP')
# myFile.close()

# # Read from file
# myFile = open('myfile.txt', 'r+')
# text = myFile.read(100)
# print(text)


# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

# import json

# #  Sample JSON
# userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# # Parse to dict
# user = json.loads(userJSON)

# # print(user)
# # print(user['first_name'])

# car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

# carJSON = json.dumps(car)

# print(carJSON)
